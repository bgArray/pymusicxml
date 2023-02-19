from .dict_to_xml import jsonToXML, formatting_xml, L
from typing import Union

from TrimLog import *

logger.license_shower("dict_to_xml", "MIT", "Copyright 2023 bgArray", "v0.4.0")

VERSION = "0.4.0"


def dict_to_xml(
    json_str: Union[str, dict],
    encoding: str = "utf-8",
    indent: str = "    ",
    is_musicxml: bool = True,
    dtd_mode: L = "web",
    dtd_path: str = """./schema/partwise.dtd">""",
) -> str:
    """Return an XML string of a Python dict object."""
    return formatting_xml(jsonToXML(json_str, encoding), indent, is_musicxml, dtd_mode, dtd_path)


__all__ = ["dict_to_xml"]
