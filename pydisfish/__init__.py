"""
PyDisFish
~~~~~~~~~~~~~~~~~~~
A teeny tiny little module to check domains against discord's phishing list
:copyright: (c) 2021-present kaj
:license: MIT, see LICENSE for more details.
"""

__title__ = 'pydisfish'
__author__ = 'kaj'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present kaj'
__version__ = '1.0'

from .search import *
from .errors import *

import asyncio

loop = asyncio.get_running_loop()
if loop is not None:
    loop.create_task(fetch_list())