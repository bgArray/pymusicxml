import os
import pathlib


replace_dict = {
    '/">Tutorial</a></b></li>':
        '/">教程</a></b></li>',
    '/">"Hello World"</a></li>':
        '/">"Hello World"（开始）</a></li>',
    '/">File Structure</a></li>':
        '/">文件结构</a></li>',
    '/">MIDI-Compatible Part</a></li>':
        '/">MIDI 兼容部分</a></li>',
    '/">Notation Basics</a></li>':
        '/">基本符号</a></li>',
    '/">Chord Symbols</a></li>':
        '/">和弦符号</a></li>',
    '/"></a></li>':
        '/">指法图</a></li>',
    '/">Percussion</a></li>':
        '/">打击乐</a></li>',
    '/">Compressed .MXL Files</a></li>':
        '/">压缩的 .MXL 文件</a></li>',
    '/">Code Generation</a></li>':
        '/">代码生成</a></li>',

    'musicxml-reference/">MusicXML Reference</a></b></li>':
        'musicxml-reference/">MusicXML 参考</a></b></li>',
    'musicxml-reference/elements/">Elements</a></li>':
        'musicxml-reference/elements/">元素</a></li>',
    'musicxml-reference/data-types/">Data Types</a></li>':
        'musicxml-reference/data-types/">数据类型</a></li>',
    'musicxml-reference/examples/">Examples</a></li>':
        'musicxml-reference/examples/">示例</a></li>',

    '/">Container Reference</a></b></li>':
        '/">Container（容器） 参考</a></b></li>',
    'container-reference/elements/">Elements</a></li>':
        'container-reference/elements/">元素</a></li>',
    'container-reference/examples/">Examples</a></li>':
        'container-reference/examples/">示例</a></li>',

    '/">Opus Reference</a></b></li>':
        '/">Opus（作品） 参考</a></b></li>',
    'opus-reference/elements/">Elements</a></li>':
        'opus-reference/elements/">元素</a></li>',
    'opus-reference/data-types/">Data Types</a></li>':
        'opus-reference/data-types/">数据类型</a></li>',
    'opus-reference/examples/">Examples</a></li>':
        'opus-reference/examples/">示例</a></li>',

    '/">Sounds Reference</a></b></li>':
        '/">Sounds（声音） 参考</a></b></li>',
    'sounds-reference/elements/">Elements</a></li>':
        'sounds-reference/elements/">元素</a></li>',
    'sounds-reference/data-types/">Data Types</a></li>':
        'sounds-reference/data-types/">数据类型</a></li>',
    'sounds-reference/examples/">Examples</a></li>':
        'sounds-reference/examples/">示例</a></li>',

    '/">Elements</a></li>':
        '/">元素</a></li>',
    'data-types/">Data Types</a></li>':
        'data-types/">数据类型</a></li>',
    'examples/">Examples</a></li>':
        'examples/">示例</a></li>',

    '/">File Listings</a></b></li>':
        '/">文件列表</a></b></li>',
    '">Version History</a></b></li>':
        '">历史版本</a></b></li>',

}


def main():
    global replace_dict
    for i in os.walk("./docs_CN/"):
        print(i[0])
        for j in os.listdir(i[0]):
            print(j)
            if pathlib.Path(j).suffix == ".html":
                try:
                    with open(
                        str(i[0] + "/" + j).replace("\\", "/"), "r", encoding="utf-8"
                    ) as f:
                        content = f.read()
                    print(content)
                    content = content.replace(
                        '/"/>Introduction</a></b></li>',
                        '/"/>介绍</a></b></li>',
                    )

                    for k in replace_dict:
                        content = content.replace(k, replace_dict[k])
                    with open(
                        str(i[0] + "/" + j).replace("\\", "/"), "w", encoding="utf-8"
                    ) as f:
                        f.write(content)
                except FileNotFoundError:
                    print(str(i[0] + "/" + j).replace("\\", "/") + " not found")


if __name__ == "__main__":
    main()
