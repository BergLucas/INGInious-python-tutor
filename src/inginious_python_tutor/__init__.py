"""Plugin entry point for INGInious-python-tutor."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from urllib.parse import quote

from docutils import nodes
from docutils.parsers.rst import Directive, directives

if TYPE_CHECKING:
    from inginious.client.client import Client
    from inginious.frontend.plugin_manager import PluginManager

__version__ = "0.1.0"


BASE_URL = "https://pythontutor.com/iframe-embed.html"

OPTION_SPEC = {
    "width": directives.nonnegative_int,
    "height": directives.nonnegative_int,
    "frameborder": directives.nonnegative_int,
    "code-div-height": directives.nonnegative_int,
    "code-div-width": directives.nonnegative_int,
    "cur-instr": directives.nonnegative_int,
}

QUERY_PARAMETERS = {
    "code-div-height": "codeDivHeight",
    "code-div-width": "codeDivWidth",
    "cur-instr": "curInstr",
    "py": "py",
}


def init(
    plugin_manager: PluginManager,
    client: Client,
    plugin_config: dict[str, Any],
) -> None:
    """Initialises the plugin by registering the reStructuredText directives.

    Args:
        plugin_manager: The plugin manager instance.
        client: The client instance.
        plugin_config: The plugin configuration dictionary. The directive
            option names it contains override the default values used by the
            ``python-tutor`` directive.
    """
    defaults: dict[str, Any] = {
        key: OPTION_SPEC[key](value)
        for key, value in plugin_config.items()
        if key in OPTION_SPEC
    }

    class PythonTutorDirective(Directive):
        """Displays Python code in an interactive Python Tutor iframe.

        The directive works like ``code-block``: its content is the code to visualise.
        """

        required_arguments = 0
        optional_arguments = 1
        final_argument_whitespace = True
        has_content = True
        option_spec = OPTION_SPEC

        def run(self) -> list[nodes.raw]:
            """Builds the Python Tutor iframe.

            Returns:
                A list containing a single raw HTML node with the ``iframe`` tag.
            """
            self.assert_has_content()

            options: dict[str, Any] = defaults | self.options

            if len(self.arguments) == 1:
                options["py"] = self.arguments[0]

            code = "\n".join(self.content)
            query_parameters = "&".join(
                (
                    f"code={quote(code, safe='')}",
                    *(
                        f"{QUERY_PARAMETERS[key]}={quote(str(value), safe='')}"
                        for key, value in options.items()
                        if key in QUERY_PARAMETERS
                    ),
                )
            )
            attributes = " ".join(
                (
                    *(
                        f'{key}="{value}"'
                        for key, value in options.items()
                        if key not in QUERY_PARAMETERS
                    ),
                    f'src="{BASE_URL}#{query_parameters}"',
                )
            )

            return [
                nodes.raw(
                    "",
                    f"<iframe {attributes}></iframe>",
                    format="html",
                )
            ]

    directives.register_directive("python-tutor", PythonTutorDirective)
