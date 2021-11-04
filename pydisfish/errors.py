class PyDisFishError(Exception):
    """Base error class for the module"""

    pass


class FetchError(PyDisFishError):
    """Error that's raised when _fetch_list() fails

    This is probably something either on your end or discord's
    """

    pass