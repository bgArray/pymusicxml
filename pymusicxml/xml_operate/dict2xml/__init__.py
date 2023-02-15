from .logic import Converter, Node

from TrimLog import *

logger.license_shower(
    "dict2xml",
    "MIT",
    "Copyright 2023 Original author of this library and bgArray",
    "1.7.2 + bgArray's modification"
)

VERSION = "1.7.2"


def dict2xml(data, *args, **kwargs):
    """Return an XML string of a Python dict object."""
    return Converter(*args, **kwargs).build(data)


__all__ = ["dict2xml", "Converter", "Node"]
