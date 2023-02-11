class XmlError(Exception):
    """Base class for exceptions in this module."""
    pass


class XmlFileError(XmlError):
    """Exception raised for errors in the input."""
    pass


class XmlConvertError(XmlError):
    """Exception raised for errors in the input."""
    pass
