class BaseTag(dict):
    def __init__(
            self,
            in_dict: dict,
    ):
        super().__init__(in_dict)

        self.attr: list = []

        self.trans_in_dict(in_dict)

    def trans_in_dict(self, trans: dict) -> None:
        if isinstance(self[list(trans.keys())[0]], dict) or \
                isinstance(self[list(trans.keys())[0]], BaseTag):

            # here means attr or children
            next_ = dict(self[list(trans.keys())[0]])
            if "@" in str(list(next_.keys())[0]):
                # here means attr
                for i in list(next_.keys()):
                    if "@" in str(i):
                        self.attr.append({str(i).replace("@", ""): next_[i]})
                        next_.pop(i)

            self[list(trans.keys())[0]] = next_

        else:
            # here means text
            pass

    def __repr__(self):
        if self.attr.__len__() == 0:
            return "BaseTag({})".format(super().__repr__())
        else:
            return "BaseTag(attr={},{})".format(self.attr, super().__repr__())


# convert dict to base_tag
def convertor(in_dict: dict) -> BaseTag:
    # Recursive dictionary
    for i in list(in_dict.keys()):
        if isinstance(in_dict[i], dict):
            in_dict[i] = convertor(in_dict[i])
    return BaseTag(in_dict)
