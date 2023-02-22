class BaseTag(dict):
    def __init__(
            self,
            in_dict: dict,
    ):
        super().__init__(in_dict)

        self.attr: list = []
        self.text: str = ""

        self.trans_in_dict(in_dict)

    def trans_in_dict(self, trans: dict) -> None:
        # if isinstance(self[list(trans.keys())[0]], dict) or \
        #         isinstance(self[list(trans.keys())[0]], BaseTag):
        #
        #     # here means attr or children
        #     next_ = dict(self[list(trans.keys())[0]])
        #     if "@" in str(list(next_.keys())[0]):
        #         # here means attr
        #         for i in list(next_.keys()):
        #             if "@" in str(i):
        #                 self.attr.append({str(i).replace("@", ""): next_[i]})
        #                 next_.pop(i)
        #
        #     self[list(trans.keys())[0]] = next_

        if "@" in str(list(trans.keys())[0]):
            for i in list(trans.keys()):
                if "@" in str(i):
                    self.attr.append({str(i).replace("@", ""): trans[i]})
                    self.pop(i)
                if str(i) == "#text":
                    self.text = trans[i]
                    self.pop(i)

    def trans_to_dict(self) -> dict:
        if self.attr.__len__() != 0:
            for i in self.attr:
                new_i = dict(i)
                for j in list(new_i.keys()):
                    new_i["@" + j] = new_i.pop(j)
                self_ = dict(self)
                self.clear()
                self.update(new_i)
                self.update(self_)
        if self.text != "":
            self.update({"#text": self.text})
        return dict(self)

    def __repr__(self):
        if self.attr.__len__() == 0 and self.text == "" and self.__len__() != 0:
            return "BaseTag({})".format(super().__repr__())
        elif self.attr.__len__() != 0 and self.text == "" and self.__len__() != 0:
            return "BaseTag(attr={},{})".format(self.attr, super().__repr__())
        elif self.attr.__len__() == 0 and self.text != "" and self.__len__() != 0:
            return "BaseTag(text={}, {})".format(self.text, super().__repr__())
        elif self.attr.__len__() != 0 and self.text != "" and self.__len__() != 0:
            return "BaseTag(attr={}, text={}, {})".format(self.attr, self.text, super().__repr__())
        elif self.attr.__len__() != 0 and self.text != "" and self.__len__() == 0:
            return "BaseTag(attr={}, text={})".format(self.attr, self.text)
        elif self.attr.__len__() == 0 and self.text == "" and self.__len__() == 0:
            return "BaseTag()"


# convert dict to base_tag
def convertor(in_dict: dict) -> BaseTag:
    # Recursive dictionary
    for i in list(in_dict.keys()):
        if isinstance(in_dict[i], dict):
            in_dict[i] = convertor(in_dict[i])
        elif isinstance(in_dict[i], list):
            for j in range(in_dict[i].__len__()):
                if isinstance(in_dict[i][j], dict):
                    in_dict[i][j] = convertor(in_dict[i][j])
                else:
                    pass
    return BaseTag(in_dict)


# convert base_tag to dict
def restorer(in_base: BaseTag) -> dict:
    for i in list(in_base.keys()):
        if isinstance(in_base[i], BaseTag):
            in_base[i] = restorer(in_base[i])
        elif isinstance(in_base[i], list):
            for j in range(in_base[i].__len__()):
                if isinstance(in_base[i][j], BaseTag):
                    in_base[i][j] = restorer(in_base[i][j])
                else:
                    pass
    return in_base.trans_to_dict()


def detector(in_base: BaseTag) -> None:
    # recursive base_tag
    for i in list(in_base.keys()):
        if isinstance(in_base[i], BaseTag):
            detector(in_base[i])
        elif isinstance(in_base[i], list):
            for j in range(in_base[i].__len__()):
                if isinstance(in_base[i][j], BaseTag):
                    detector(in_base[i][j])
                else:
                    pass
        elif isinstance(in_base[i], dict):
            print("error: {}".format(in_base[i]))
