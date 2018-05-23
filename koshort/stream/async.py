"""Experimental implementation of asynchronous request using asyncio"""

import sys

if not (sys.version_info[0] >= 3) & (sys.version_info[1] >= 5):
    raise Exception("Asynchrounous API is only available python3.5 or newer.")

import asyncio
import aiohttp
import collections
import warnings


def _process(response):
    """Dummy post-processing after http request"""
    pass


class Request(object):
    def __init__(self, process=_process):
        """Asynchronous request API
        
        Args:
            process (callable, optional): Defaults to _process.
                pass a custom processing function after getting response if needed.
        """

        assert callable(process)
        self.header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}
    
    async def get(self, url, process=_process):
        """Asynchronous get request and custom postprocessing
        
        Args:
            url (str): url to request get
            process (callable, optional): Defaults to _process. 
                pass a custom processing function after getting response if needed.
        """
        assert isinstance(url, str)

        connector = aiohttp.TCPConnector(limit=16)
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url, headers=self.header) as response:
                return process(response)

    def run(self, tasks):
        """Run asynchronous event loop until complete
        
        Args:
            tasks (collections.Iterable): Iterable tasks to be executed
        """

        if not isinstance(tasks, collections.Iterable):
            tasks = [tasks]

        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(asyncio.wait(tasks))
        except ValueError:
            loop.close()
