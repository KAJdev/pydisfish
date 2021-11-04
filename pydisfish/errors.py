class PyDisFishError(Exception):
    """Base error class for the module"""

    pass


class FetchError(PyDisFishError):
    """Error that's raised when _fetch_list() fails

    This is probably something either on your end or discord's
    """

    pass


class NotReady(PyDisFishError):
    """Error that's raised when trying to check a URL before Phisherman is ready

    you should use Phisherman.ready to tell when the domain list has been fetched
    """
    
    pass
