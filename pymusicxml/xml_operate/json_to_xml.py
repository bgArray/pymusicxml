# Converting Python Dictionary to XML
from dict2xml import dict2xml


def dict_to_xml(dict_data: dict) -> str:
    xml = dict2xml(dict_data)
    return xml
