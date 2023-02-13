from pymusicxml import *
from TrimLog import *

logger.info("TrimLog is working.")

if __name__ == "__main__":
    xml_to_json("./pymusicxml/resources/Hello World in MusicXML.musicxml")
    meta_ex = xml_to_json("./pymusicxml/resources/metaExample.musicxml", False)
    osc = ObjectStateConstant()
    osc.set_console(logger.console)
    osc.dp(meta_ex)

    # test_parse("./pymusicxml/resources/metaExample.musicxml")
