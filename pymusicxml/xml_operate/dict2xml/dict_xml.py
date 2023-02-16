# change dict into xml string

import sys

sys.setrecursionlimit(1000000)

# for test
test1 = {'score-partwise': {'@version': '4.0', 'work': {'work-number': 'D. 911', 'work-title': 'Winterreise'},
                            'movement-number': '22', 'movement-title': 'Mut', 'identification': {
        'creator': [{'@type': 'composer', '#text': 'Franz Schubert'}, {'@type': 'poet', '#text': 'Wilhelm Müller'}],
        'rights': 'Copyright © 2001 Recordare LLC',
        'encoding': {'encoding-date': '2002-02-16', 'encoder': 'Michael Good', 'software': 'Finale 2002 for Windows',
                     'encoding-description': 'MusicXML 1.0 example'},
        'source': 'Based on Breitkopf & Härtel edition of 1895'}, 'part-list': {
        'score-part': [{'@id': 'P1', 'part-name': 'Singstimme.'}, {'@id': 'P2', 'part-name': 'Pianoforte.'}]}}}


# def _dict_2_xml(dict_data: dict) -> str:
#     # xml = Converter().build(dict_data)
#     xml = Converter()
#     xml = xml.walk(dict_data)
#     return xml


# def walk(data: dict):
#     print(data)
#     print("a")
#     for key in data.keys():  # 当前迭代的字典
#         data = data[key]  # 当前key所对应的value赋给data
#
#         print(data)
#
#         if isinstance(data, dict):  # 如果data是一个字典，就递归遍历
#             print("c")
#             return walk(data)
#         else:
#             is_end = True
#             for j in data:
#                 if isinstance(j, dict):
#                     is_end = False
#                     break
#             if is_end:
#                 return key, data

def walk(data: dict):
    pass


if __name__ == '__main__':
    # xml_ = _dict_2_xml(test1)
    # print(xml_)
    for i in walk(test1):
        print(i)
    # import os
