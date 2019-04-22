import pkgutil
import importlib
import alglbraic
import click


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    ignore_starts_with = ("snapshots", "__", "test_")

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


submodules = import_submodules(alglbraic)

subcommands = []

for (_, sub) in submodules.items():
    try:
        subcommands.append(sub.commands)
    except AttributeError:
        pass


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


@click.command(cls=click.CommandCollection, sources=subcommands, chain=True)
@click.option("--out", type=click.Path())
@click.option("--glslify", is_flag=True)
@click.pass_context
def cli(ctx, out, glslify, **opts):
    ctx.obj["out"] = out
    ctx.obj["glslify"] = glslify 


@cli.resultcallback()
@click.pass_obj
def process_result(obj, *args, **opts):
    import os

    bundles = OrderedDict(
        [(name, bundler.bundle()) for (name, bundler) in obj["results"].items()]
    )

    out = obj.get("out")
    glslify = obj.get("glslify")
    if out:
        existed = os.path.exists(out)
        if not existed:
            os.makedirs(out)
        os.chdir(out)
        if glslify:
            os.remove('index.glsl')
            index = open('index.glsl', 'a+')
        for (name, bundle) in bundles.items():
            if glslify:
                index.write(f"// {name}.glsl\n#pragma glslify: import('./{name}.glsl')\n\n")
            f = open(f"{name}.glsl", "w")
            f.write(bundle)
            f.close()
        if glslify:
            index.close()
    else:
        for (name, bundle) in bundles.items():
            click.echo(bundle)


if __name__ == "__main__":
    from collections import OrderedDict

    cli(obj={"results": OrderedDict()})


# class ConfigSectionSchema(object):

#     @matches_section("foo")
#     class Foo(SectionSchema):
#         name    = Param(type=str)
#         flag    = Param(type=bool, default=True)
#         numbers = Param(type=int, multiple=True)
#         filenames = Param(type=click.Path(), multiple=True)

#     @matches_section("person.*")   # Matches multiple sections
#     class Person(SectionSchema):
#         name      = Param(type=str)
#         birthyear = Param(type=click.IntRange(1990, 2100))


# class ConfigFileProcessor(ConfigFileReader):
#     config_files = ["alglbraic.ini", "alglbraic.cfg"]
#     # config_section_schemas = []


# # -- COMMAND:
# CONTEXT_SETTINGS = dict(default_map=ConfigFileProcessor.read_config())


# @click.command(context_settings=CONTEXT_SETTINGS)
# # @click.option("-n", "--number", "numbers", type=int, multiple=True)
# @click.pass_context
# def command_with_config(ctx, numbers):
#     pass
#     # -- ACCESS ADDITIONAL DATA FROM CONFIG FILES: Using ctx.default_map
#     # for person_data_key in ctx.default_map.keys():
#     #     if not person_data_key.startswith("person."):
#     #         continue
#     #     person_data = ctx.default_map[person_data_key]
#     #     process_person_data(person_data)    # as dict.


# # @click.group()
# # @click.option('--debug/--no-debug', default=False)
# # def cli(debug):
# #     click.echo('Debug mode is %s' % ('on' if debug else 'off'))

# # import click

