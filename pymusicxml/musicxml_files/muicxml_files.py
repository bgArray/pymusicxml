import pathlib

from typing import Union


class MusicxmlFile(object):
    def __init__(self,
                 file: Union[str, pathlib.Path] = None,
                 ):

        if file is not None:
            if isinstance(file, str):
                file = pathlib.Path(file)
            self.file = file
