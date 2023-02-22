from .exceptions import *
from .xml_to_json import xml_to_json
from .dict_to_xml import dict_to_xml

from .schema import *

from .base_tag import BaseTag, convertor, detector, restorer

from TrimLog import *

logger.license_shower(
    "xml_operate",
    "Apache-2.0",
    "Copyright 2023 bgArray",
    "v0.2.0"
)
