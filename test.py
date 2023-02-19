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

    print(dict_to_xml(meta_ex))
    with open("a.musicxml", "w", encoding="utf-8") as f:
        f.write(
            dict_to_xml(
                meta_ex,
                dtd_mode="local",
                dtd_path="""./pymusicxml/xml_operate/schema/partwise.dtd">""",
            )
        )

    # test_parse("./pymusicxml/resources/metaExample.musicxml")
