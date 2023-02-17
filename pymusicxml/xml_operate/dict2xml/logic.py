import collections.abc
import collections
import re

start_ranges = "|".join(
    "[{0}]".format(r)
    for r in [
        "\xC0-\xD6",
        "\xD8-\xF6",
        "\xF8-\u02FF",
        "\u0370-\u037D",
        "\u037F-\u1FFF",
        "\u200C-\u200D",
        "\u2070-\u218F",
        "\u2C00-\u2FEF",
        "\u3001-\uD7FF",
        "\uF900-\uFDCF",
        "\uFDF0-\uFFFD",
    ]
)

NameStartChar = re.compile(r"(:|[A-Z]|_|[a-z]|{0})".format(start_ranges))
NameChar = re.compile(r"(-|\.|[0-9]|\xB7|[\u0300-\u036F]|[\u203F-\u2040])")


########################
# ##   NODE
########################


class Node(object):
    """
    Represents each tag in the tree

    Each node has _either_ a single value or one or more children
    If it has a value:
        The serialized result is <%(tag)s>%(value)s</%(tag)s>

    If it has children:
        The serialized result is
            <%(wrap)s>
                %(children)s
            </%(wrap)s>

    Which one it is depends on the implementation of self.convert
    """

    # A mapping of characters to treat as escapable entities and their replacements
    entities = [("&", "&amp;"), ("<", "&lt;"), (">", "&gt;")]

    def __init__(
        self,
        wrap="",
        tag="",
        data=None,
        iterables_repeat_wrap=True,
        closed_tags_for=None,
    ):
        self.tag = self.sanitize_element(tag)
        self.wrap = self.sanitize_element(wrap)
        self.data = data
        self.type = self.determine_type()
        self.closed_tags_for = closed_tags_for
        self.iterables_repeat_wrap = iterables_repeat_wrap

        print("Node.__init__(): self.tag = {0}".format(self.tag))
        print("Node.__init__(): self.wrap = {0}".format(self.wrap))
        print("Node.__init__(): self.data = {0}".format(self.data))
        print("Node.__init__(): self.type = {0}".format(self.type))
        print("Node.__init__(): self.closed_tags_for = {0}".format(self.closed_tags_for))
        print("Node.__init__(): self.iterables_repeat_wrap = {0}".format(self.iterables_repeat_wrap))

        if self.type == "flat" and isinstance(self.data, str):
            # Make sure we deal with entities
            for entity, replacement in self.entities:
                self.data = self.data.replace(entity, replacement)

    def serialize(self, indenter):
        """Returns the Node serialized as a xml string"""
        # Determine the start and end of this node
        wrap = self.wrap
        end, start = "", ""
        if wrap:
            end = "</{0}>".format(wrap)
            start = "<{0}>".format(wrap)

        if self.closed_tags_for and self.data in self.closed_tags_for:
            return "<{0}/>".format(self.wrap)

        # Convert the data attached in this node into a value and children
        value, children = self.convert()

        # Determine the content of the node (essentially the children as a string value)
        content = ""
        if children:
            if self.type != "iterable":
                # Non-iterable wraps all it's children in the same tag
                content = indenter((c.serialize(indenter) for c in children), wrap)
            else:
                if self.iterables_repeat_wrap:
                    # Iterables repeat the wrap for each child
                    result = []
                    for c in children:
                        content = c.serialize(indenter)
                        if c.type == "flat":
                            # Child with value, it already is surrounded by the tag
                            result.append(content)
                        else:
                            # Child with children of it's own, they need to be wrapped by start and end
                            content = indenter([content], True)
                            result.append("".join((start, content, end)))

                    # We already have what we want, return the indented result
                    return indenter(result, False)
                else:
                    result = []
                    for c in children:
                        result.append(c.serialize(indenter))
                    return "".join([start, indenter(result, True), end])

        # If here, either:
        #  * Have a value
        #  * Or this node is not an iterable
        return "".join((start, value, content, end))

    def determine_type(self):
        """
        Return the type of the data on this node as an identifying string

        * Iterable : Supports "for item in data"
        * Mapping : Supports "for key in data: value = data[key]"
        * flat : A string or something that isn't iterable or a mapping
        """
        data = self.data
        if isinstance(data, str):
            return "flat"
        elif isinstance(data, collections.abc.Mapping):
            return "mapping"
        elif isinstance(data, collections.abc.Iterable):
            return "iterable"
        else:
            return "flat"

    def convert(self):
        """
        Convert data on this node into a (value, children) tuple depending on the type of the data
        If the type is :
            * flat : Use self.tag to surround the value. <tag>value</tag>
            * mapping : Return a list of tags where the key for each child is the wrap for that node
            * iterable : Return a list of Nodes where self.wrap is the tag for that node
        """
        val = ""
        typ = self.type
        data = self.data
        children = []

        if typ == "mapping":
            sorted_data = data
            if not isinstance(data, collections.OrderedDict):
                sorted_data = sorted(data)

            for key in sorted_data:
                item = data[key]
                children.append(
                    Node(
                        key,
                        "",
                        item,
                        iterables_repeat_wrap=self.iterables_repeat_wrap,
                        closed_tags_for=self.closed_tags_for,
                    )
                )

        elif typ == "iterable":
            for item in data:
                children.append(
                    Node(
                        "",
                        self.wrap,
                        item,
                        iterables_repeat_wrap=self.iterables_repeat_wrap,
                        closed_tags_for=self.closed_tags_for,
                    )
                )

        else:
            val = str(data)
            if self.tag:
                val = "<{0}>{1}</{2}>".format(self.tag, val, self.tag)

        return val, children

    @staticmethod
    def sanitize_element(wrap):
        """
        Convert `wrap` into a valid tag name applying the XML Naming Rules.

            * Names can contain letters, numbers, and other characters
            * Names cannot start with a number or punctuation character
            * Names cannot start with the letters xml (or XML, or Xml, etc)
            * Names cannot contain spaces
            * Any name can be used, no words are reserved.

        :ref: http://www.w3.org/TR/REC-xml/#NT-NameChar
        """
        if wrap and isinstance(wrap, str):
            if wrap.lower().startswith("xml"):
                wrap = "_" + wrap
            return "".join(
                ["_" if not NameStartChar.match(wrap) else ""]
                + [
                    "_" if not (NameStartChar.match(c) or NameChar.match(c)) else c
                    for c in wrap
                ]
            )
        else:
            return wrap


########################
# ##   CONVERTER
########################


class Converter(object):
    """Logic for creating a Node tree and serialising that tree into a string
       用于创建节点树并将该树串行化为字符串的逻辑
    """

    def __init__(self, wrap=None, indent="  ", newlines=True) -> None:
        """
        :param wrap: The tag that everything else will be contained within
        其他所有内容都将包含在其中的标记
        :param indent: The string that is multiplied at the start of each new line, to represent each level of nesting
        在每一新行开始处相乘的字符串，以表示每一嵌套级别
        :param newlines: A boolean specifying whether we want each tag on a new line.
        一个布尔值，指定我们是否希望每一个标记位于新行上。

        Note that indent only works if newlines is True
        注意，缩进仅在换行符为True时有效
        """
        self.wrap = wrap
        self.indent = indent
        self.newlines = newlines

    def _make_indenter(self):
        """Returns a function that given a list of strings, will return that list as a single, indented, string
        返回给定字符串列表的函数，将该列表作为单个缩进字符串返回"""
        indent = self.indent
        newlines = self.newlines

        if not newlines:
            # No newlines, don't care about indentation 没有换行符，不在乎缩进
            # Pymusicxml don't use it in default.  Pymusicxml默认情况下不使用它。
            ret = lambda nodes, wrapped: "".join(nodes)
        else:
            if not indent:
                indent = ""

            def each_line(nodes):
                """Yield each line in each node 在每个节点中 yield 每一行"""
                for node in nodes:
                    for line in node.split("\n"):
                        yield line

            def ret(nodes, wrapped):
                """
                Indent nodes depending on value of wrapped and indent
                If not wrapped, then don't indent
                Otherwise,
                Separate each child by a newline
                and indent each line in the child by one indent unit

                根据换行和缩进的值 缩进节点
                如果未换行，则不缩进
                否则
                用换行符分隔每个子项
                并将子级中的每行缩进一个缩进单位
                """
                if wrapped:
                    seperator = "\n{0}".format(indent)
                    surrounding = "\n{0}{{0}}\n".format(indent)
                else:
                    seperator = "\n"
                    surrounding = "{0}"
                return surrounding.format(seperator.join(each_line(nodes)))

        return ret

    def build(self, data, iterables_repeat_wrap=True, closed_tags_for=None):
        """Create a Node tree from the data and return it as a serialized xml string"""
        indenter = self._make_indenter()
        return Node(
            wrap=self.wrap,
            data=data,
            iterables_repeat_wrap=iterables_repeat_wrap,
            closed_tags_for=closed_tags_for,
        ).serialize(indenter)
