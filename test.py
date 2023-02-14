from pymusicxml import *
from TrimLog import *

logger.info("TrimLog is working.")

if __name__ == "__main__":
    refresh_schema_list()
    # xml_to_json("./pymusicxml/resources/Hello World in MusicXML.musicxml")
    xml_to_json("./pymusicxml/resources/test_dtd.musicxml")
    meta_ex = xml_to_json("./pymusicxml/resources/metaExample.musicxml", False)
    print(meta_ex)
    osc = ObjectStateConstant()
    osc.set_console(logger.console)
    osc.dp(meta_ex)

    # test_parse("./pymusicxml/resources/metaExample.musicxml")
