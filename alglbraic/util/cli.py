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

cli = click.CommandCollection(sources=subcommands)

if __name__ == "__main__":
    cli()

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

