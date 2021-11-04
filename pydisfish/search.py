from . import __version__
from .errors import *

from typing import List
import hashlib

import aiohttp
import asyncio

_headers = {
    'User-Agent': f'PyDisFish {__version__} (https://github.com/kajdev/pydisfish)'
}


phishing_list = []

async def fetch_list(url: str = "https://cdn.discordapp.com/bad-domains/hashes.json") -> List[str]:
    """
    Fetch the list of sha256 hashes from discord's CDN
    """

    async with aiohttp.ClientSession(headers=_headers) as session:
        async with session.get(url) as response:

            if response.status == 200:
                phishing_list = await response.json()

            else:
                raise FetchError(f"Error fetching hash list: {response.status}")


def check(url: str) -> bool:
    """
    Check a URL against discord's phishing domain list
    """

    return hashlib.sha256(url.encode('utf-8')).hexdigest() in phishing_list