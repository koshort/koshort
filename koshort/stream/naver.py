# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from urllib.request import urlopen
from bs4 import BeautifulSoup
from threading import Thread
from koshort.data import StringWriter
from time import sleep
from argparse import ArgumentParser


class NaverStreamer(object):
    """NaverStreamer helps to stream naver trending keywords asynchronously.
    
    ..code-block:: python

        >>> from koshort.stream import naver
        >>> streamer = naver.NaverStreamer()
        >>> streamer.stream()
        cj채용
        온주완의 뮤직쇼
        유상무
        현대차
        ...

    """

    def __init__(self):
        parser = self.get_parser()

        self.url = 'https://www.naver.com/'
        self.args = parser.parse_args()
        self.writer = StringWriter(self.args.filename)

    @staticmethod
    def get_parser():
        """customized argument parser to set various parameters

        Returns:
            object: argument parser.
        """

        p = ArgumentParser()
        p.add_argument(
            '-v', '--verbose', 
            help="increase verbosity", 
            action="store_true"
        )
        p.add_argument(
            '-d', '--display_rank', 
            help="display rank in results and commandline.", 
            action="store_true"
        )
        p.add_argument(
            '-i', '--interval', 
            help="streaming interval(secs)", 
            type=int
        )
        p.add_argument(
            '-n', '--n_limits', 
            help="stop when this amount of trends are collected. 0 for forever", 
            default=10,
            type=int
        )
        p.add_argument(
            '--filename', 
            help="filename to be saved.", 
            default="trends.txt"
        )
        return p

    def get_current_trend(self):
        """Get current top trending words
        
        Returns:
            counts: list of count
            keywords: list of keyword
        """

        html = urlopen(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        counts = []
        keywords = []

        for item in soup.find("div", {"class":"ah_roll_area PM_CL_realtimeKeyword_rolling"}).findAll("li", {"class":"ah_item"}):
            count = item.find("span", {"class":"ah_r"}).getText()
            keyword = item.find("span", {"class":"ah_k"}).getText()
            counts.append(count)
            keywords.append(keyword)
        
        return counts, keywords

    def save_and_print(self):
        """collect current trending words and save or print"""

        counts, keywords = self.get_current_trend()

        if self.args.display_rank:
            for count, keyword in zip(counts, keywords):
                pair = "{}.{}".format(count, keyword)
                self.writer.write(pair)
                if self.args.verbose:
                    print(pair)
                
        else:
            for keyword in keywords:
                self.writer.write(keyword)
                if self.args.verbose:
                    print(keyword)

    def job(self, interval):
        """Streaming job with intervals.
        
        Args:
            interval (int): Time interval
        """

        n_try = 0
        while (self.args.n_limits == 0) | (self.args.n_limits > n_try):
            n_try += 1
            self.save_and_print()
            sleep(interval)

    def stream(self, interval=60, async=True):
        if async:
            self._thread = Thread(target=lambda: self.job(interval))
            self._thread.start()
        else:
            self.job(interval)