class BaseTag(dict):
    def __init__(
        self,
        in_dict: dict,
    ):
        super().__init__(in_dict)

        self.attr: list = []

        self.trans_in_dict(in_dict)

        self.tag = None
        self.text = None

        self.children = None

    def trans_in_dict(self, trans: dict) -> None:
        if isinstance(self[list(trans.keys())[0]], dict) or isinstance(self[list(trans.keys())[0]], BaseTag):
            # here means attr or children

            next_ = dict(self[list(trans.keys())[0]])
            if "@" in str(list(next_.keys())[0]):
                # here means attr
                for i in list(next_.keys()):
                    if "@" in str(i):
                        self.attr.append({str(i).replace("@", ""): next_[i]})

        else:
            # here means text
            pass
