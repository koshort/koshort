"""Experimental implemntation of asynchronous request using asyncio"""

import sys

if not (sys.version_info[0] >= 3) & (sys.version_info[1] >= 5):
    raise Exception("Asynchrounous API is only available python3.5 or newer.")

import asyncio
import aiohttp


class AsyncStreamer(object):
    """Asynchronous request is much much faster way to do everything"""

    def __init__(self, process, url, init_point, end_point):
        assert callable(process)
        self.process = process
        self.url = url
        self.init_point = init_point
        self.end_point = end_point
        self.header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

    async def task(self, i, process):
        connector = aiohttp.TCPConnector(limit=16)
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(self.url+i, headers=self.header) as response:
                process(response)

    def stream(self):
        tasks = [self.task(idx, self.process) for idx in range(self.init_point, self.end_point)]
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(asyncio.wait(tasks))
        except ValueError:
            loop.close()