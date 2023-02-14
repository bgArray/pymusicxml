import os

schema_list = ['attributes.mod', 'barline.mod', 'catalog.xml', 'common.mod', 'container.dtd', 'container.xsd',
               'direction.mod', 'identity.mod', 'isolat1.ent', 'isolat2.ent', 'layout.mod', 'link.mod', 'midixml.dtd',
               'midixml.xsl', 'musicxml.xsd', 'note.mod', 'opus.dtd', 'opus.xsd', 'parttime.xsl', 'partwise.dtd',
               'score.mod', 'sounds.dtd', 'sounds.xml', 'sounds.xsd', 'timepart.xsl', 'timewise.dtd', 'to10.xsl',
               'to11.xsl', 'to20.xsl', 'to30.xsl', 'to31.xsl', 'xlink.xsd', 'xml.xsd']


def refresh_schema_list():
    global schema_list
    current_work_dir = os.path.dirname(__file__)  # 当前文件所在的目录
    # weight_path = os.path.join(current_work_dir, "schema")
    # weight_path = os.path.join(current_work_dir, weight_path)  # 再加上它的相对路径，这样可以动态生成绝对路径
    schema_list = os.listdir(current_work_dir)


__all__ = ["schema_list",
           "refresh_schema_list"]
