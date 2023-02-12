import xmltojson
import pathlib
from typing import Union

from .exceptions import *


def xml_to_json(file: Union[str, pathlib.Path], is_fragment: bool = True) -> dict:
    if isinstance(file, str):
        file = pathlib.Path(file)  # convert str to Path

    if not file.exists():
        raise FileNotFoundError(f"File {file} not found.")

    if file.suffix != ".musicxml":
        raise FileNotFoundError(f"File {file} is not a musicxml file.")

    if is_fragment:
        with open(file, "r", encoding="utf-8") as f:  # check if the file is a musicxml file
            first_line = f.readline()
            if (
                first_line
                != """<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n"""
                and first_line != """<?xml version="1.0" encoding="UTF-8"?>\n"""
            ):
                raise XmlFileError(
                    f"File {file} is not a musicxml file.\nPlease check your musicxml's second line."
                )

        with open(file, "r", encoding="utf-8") as f:  # check if the file is a musicxml file
            f_1 = f.read(-1)

            second_line = (
                "<!DOCTYPE score-partwise PUBLIC",
                '"-//Recordare//DTD MusicXML 4.0 Partwise//EN"',
                '"http://www.musicxml.org/dtds/partwise.dtd">',
            )

            for i in second_line:
                if i not in f_1:
                    raise XmlFileError(
                        f"File {file} is not a musicxml file.\nPlease check your musicxml's headline."
                    )

    with open(file, "r", encoding="utf-8") as f:
        xml = f.read()
        if xml == "":
            raise XmlFileError(f"File {file} is empty.")

    try:
        json_ = xmltojson.parse(xml)
        json_ = eval(json_)  # convert str to dict
    # noinspection PyBroadException
    except Exception as e:
        raise XmlConvertError(f"File {file} convert to json failed.\n{e}")
    return json_


if __name__ == "__main__":
    path = (
        "L:\\2PythonMusicXMLProcessor\\pymusicxml\\master-0.0.1\\pymusicxml\\pymusicxml\\resources"
        "\\Hello World in MusicXML.musicxml"
    )
    result = xml_to_json(path)
    print(result["score-partwise"]["part-list"]["score-part"]["part-name"])
