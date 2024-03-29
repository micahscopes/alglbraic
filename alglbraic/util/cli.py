import pkgutil
import importlib
import alglbraic
import click
from collections import OrderedDict


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    ignore_starts_with = ("snapshots", "__", "test_", "snap_test")

    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + "." + name
        if not name.startswith(ignore_starts_with):
            results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


def get_subcommands(modules=[]):
    subcommands = []

    for mod in modules:
        submodules = import_submodules(mod)

        for (_, sub) in submodules.items():
            try:
                subcommands.append(sub.commands)
            except AttributeError:
                pass

    return subcommands


class GroupWithCommandOptions(click.Group):
    """ Allow application of options to group with multi command """

    def add_command(self, cmd, name=None):
        click.Group.add_command(self, cmd, name=name)

        # add the group parameters to the command
        for param in self.params:
            cmd.params.append(param)

        # hook the commands invoke with our own
        cmd.invoke = self.build_command_invoke(cmd.invoke)
        self.invoke_without_command = True

    def build_command_invoke(self, original_invoke):
        def command_invoke(ctx):
            """ insert invocation of group function """

            # separate the group parameters
            ctx.obj = dict(_params=dict())
            for param in self.params:
                name = param.name
                ctx.obj["_params"][name] = ctx.params[name]
                del ctx.params[name]

            # call the group function with its parameters
            params = ctx.params
            ctx.params = ctx.obj["_params"]
            self.invoke(ctx)
            ctx.params = params

            # now call the original invoke (the command)
            original_invoke(ctx)

        return command_invoke


def build_cli(subcommands=[], modules=[alglbraic]):
    subcommands += get_subcommands(modules)

    @click.command(cls=click.CommandCollection, sources=subcommands, chain=True)
    @click.option("--out", type=click.Path())
    @click.option("--glslify", is_flag=True)
    @click.option("--glslify-append", is_flag=True)
    @click.pass_context
    def cli(ctx, out, glslify, glslify_append, **opts):
        ctx.obj = {"results": OrderedDict()}
        ctx.obj["out"] = out
        ctx.obj["glslify"] = glslify
        ctx.obj["glslify_append"] = glslify_append

    @cli.resultcallback()
    @click.pass_obj
    def process_result(obj, *args, **opts):
        import os

        bundles = OrderedDict(
            [(name, bundler.bundle()) for (name, bundler) in obj["results"].items()]
        )

        out = obj.get("out")
        glslify_append = obj.get("glslify_append")
        glslify = obj.get("glslify") or glslify_append
        if out:
            existed = os.path.exists(out)
            if not existed:
                os.makedirs(out)
            os.chdir(out)
            if glslify:
                if os.path.exists("index.glsl") and not glslify_append:
                    os.remove("index.glsl")
                index = open("index.glsl", "a+")
            for (name, bundle) in bundles.items():
                if glslify:
                    index.write(
                        f"// {name}.glsl\n#pragma glslify: import('./{name}.glsl')\n\n"
                    )
                f = open(f"{name}.glsl", "w")
                f.write(bundle)
                f.close()
            if glslify:
                index.close()
        else:
            for (name, bundle) in bundles.items():
                click.echo(bundle)

    return cli


@click.command()
def dummy():
    click.echo("I M DUM")

cli = build_cli()

if __name__ == "__main__":
    cli()