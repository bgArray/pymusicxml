import json
import xmltodict

from typing import Union, Literal

WEB_FORMAT = """<!DOCTYPE score-partwise PUBLIC
        "-//Recordare//DTD MusicXML 4.0 Partwise//EN"
        "http://www.musicxml.org/dtds/partwise.dtd">"""

LOCAL_FORMAT = """<!DOCTYPE score-partwise PUBLIC
    "-//Recordare//DTD MusicXML 4.0 Partwise//EN"
    "./schema/partwise.dtd">"""

L = Literal["web", "local"]


def jsonToXML(json_str: Union[str, dict], encoding: str = "utf-8") -> str:
    """传入字典字符串或字典，返回xml字符串"""
    # ————————————————
    # 版权声明：本文为CSDN博主「yujkss」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
    # 原文链接：https://blog.csdn.net/qq_39900031/article/details/115498786
    xml_str = ""
    if type(json_str) == dict:
        dic = json_str
    else:
        dic = json.loads(json_str)

    try:
        xml_str = xmltodict.unparse(dic, encoding=encoding)  # 示例字典字符串下这段代码会报错
    # noinspection PyBroadException
    except BaseException as e:
        print(e)
        xml_str = xmltodict.unparse(
            {"request": dic}, encoding=encoding
        )  # request可根据需求修改，目的是为XML字符串提供顶层标签
    finally:
        return xml_str


def formatting_xml(
    xml_str: str,
    indent: str = "    ",
    is_musicxml: bool = True,
    dtd_mode: L = "web",
    dtd_path: str = """./schema/partwise.dtd">""",
) -> str:
    """传入xml字符串，返回格式化后的xml字符串"""
    xml_str = xml_str.replace("><", ">\n<")

    global WEB_FORMAT, LOCAL_FORMAT

    # write indent into xml
    xml_list = xml_str.split("\n")
    xml_list = [i for i in xml_list if i != ""]
    xml_list = [i for i in xml_list if i != "\n"]
    xml_list = [i for i in xml_list if i != "\t"]
    xml_list = [i for i in xml_list if i != " "]
    xml_list = [i for i in xml_list if i != "\r"]

    # ————————————————
    result_str: str = ""
    if is_musicxml:
        result_str += """<?xml version="1.0" encoding="UTF-8" standalone="no"?>""" + "\n"
        if dtd_mode == "web":
            result_str += WEB_FORMAT + "\n"
        elif dtd_mode == "local":
            result_str += LOCAL_FORMAT.replace('./schema/partwise.dtd">', dtd_path) + "\n"
        else:
            result_str += WEB_FORMAT + "\n"
    else:
        result_str += xml_list[0] + "\n"
    xml_list = xml_list[1:]

    def write_indent(indent_str: str = "    ", indent_num: int = 1) -> str:
        result = ""
        for i in range(indent_num):
            result += indent_str
        return result

    now_indent = 0
    for i in xml_list:
        if i[0] == "<" and i[1] != "/":  # <note> or <note ...>
            result_str += write_indent(indent, now_indent) + i + "\n"
            if i.count(">") == 1 and i.count("<") == 1:
                now_indent += 1
        elif i[0] == "<" and i[1] == "/":  # </note>
            result_str += write_indent(indent, now_indent - 1) + i + "\n"
            now_indent -= 1
        else:  # <pitch>...</pitch>
            result_str += write_indent(indent, i.count("<")) + i + "\n"
    return result_str
