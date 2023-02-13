from .tests import fixtures_dir
from .tests.fixtures.primer import PurchaseOrder, Usaddress

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.context import XmlContext

from pathlib import Path

from typing import Union


def test_parse(file: Union[str, Path]) -> None:  # Here are some problems.
    if isinstance(file, str):
        file = Path(file)
    path = file.resolve()

    path = str(fixtures_dir.joinpath("primer/sample.xml"))

    # filename = path
    parser = XmlParser(context=XmlContext())
    # with open(filename, "r", encoding="utf-8") as f:
    #     order = parser.parse(f, PurchaseOrder)
    order = parser.parse(path, PurchaseOrder)
    print(order.bill_to)
