"""ntc_templates.parse."""
import os
import ntc_templates
import typing
import types
import netdisc.ssh

self = __import__(__name__)

# Due to TextFSM library issues on Windows, it is better to not fail on import
# Instead fail at runtime (i.e. if method is actually used).
try:
    from textfsm import clitable

    HAS_CLITABLE = True
except ImportError:
    HAS_CLITABLE = False


def get_template_dir(module: types.ModuleType = netdisc.ssh) -> str:
    templates_dir = os.path.dirname(module.__file__)
    template_dir = os.path.join(templates_dir, "templates")
    if not os.path.isdir(template_dir):
        raise RuntimeError(f"Invalid ntc_templates directory for module: {module!r}")
    return template_dir


def _clitable_to_dict(cli_table):
    """Convert TextFSM cli_table object to list of dictionaries."""
    objs = []
    for row in cli_table:
        temp_dict = {}
        for index, element in enumerate(row):
            temp_dict[cli_table.header[index].lower()] = element
        objs.append(temp_dict)

    return objs


def parse_output(
    platform=None,
    command=None,
    data=None,
    use_custom=False,
):
    """Return the structured data based on the output from a network device."""

    if use_custom:
        template_dir = get_template_dir()
    else:
        template_dir = get_template_dir(ntc_templates)
    cli_table = clitable.CliTable("index", template_dir)

    attrs = {"Command": command, "Platform": platform}
    try:
        cli_table.ParseCmd(data, attrs)
        structured_data = _clitable_to_dict(cli_table)
    except clitable.CliTableError as e:
        raise Exception(
            'Unable to parse command "{0}" on platform {1} - {2}'.format(
                command, platform, str(e)
            )
        )
        # Invalid or Missing template
        # module.fail_json(msg='parsing error', error=str(e))
        # rather than fail, fallback to return raw text
        # structured_data = [data]

    return structured_data
