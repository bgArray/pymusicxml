# Converting Python Dictionary to XML
from .dict2xml import dict2xml
from dicttoxml import dicttoxml


def dict_2_xml(dict_data: dict) -> str:
    xml = dict2xml(dict_data)
    return xml


def dict_to_xml(dict_data: dict) -> str:
    xml = dicttoxml(dict_data)
    xml = xml.decode("utf-8")
    xml = xml.replace("<root>", "").replace("</root>", "")
    xml = xml.replace(">", ">\n").replace("</", "\n</")
    return xml
