from . import __version__
from .errors import *
from .utils import *

from typing import List
import hashlib

import aiohttp
import asyncio

class Phisherman():
    """
    Class for managing discord's phishing list
    """

    def __init__(self, **options) -> None:
        self.phishing_list: List = []
        self.options: Dict = options

        self._headers: Dict = options.get('headers', 
            {'User-Agent': f'PyDisFish {__version__} (https://github.com/kajdev/pydisfish)'}
        )

        self.ready: bool = False

        loop = asyncio.get_event_loop()
        if loop is not None:
            loop.run_until_complete(self.fetch())

    async def fetch(self) -> None:
        """
        Fetch the list of sha256 hashes from discord's CDN
        """

        url = self.options.get('url',
            "https://cdn.discordapp.com/bad-domains/hashes.json"
        )

        async with aiohttp.ClientSession(headers=self._headers) as session:
            async with session.get(url) as response:

                if response.status == 200:
                    self.phishing_list = await response.json()
                    self.ready = True

                else:
                    raise FetchError(f"Error fetching hash list: {response.status}")

    def check(self, url: str) -> bool:
        """
        Check a URL against discord's phishing domain list
        """
        if not self.ready:
            raise NotReady()

        return hashlib.sha256(get_domain(url).encode('utf-8')).hexdigest() in self.phishing_list