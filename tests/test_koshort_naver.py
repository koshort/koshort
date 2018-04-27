# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from koshort.stream.naver import NaverStreamer
from koshort.constants import DATA_DIR
import glob


def test_naver_streamer():
    naver = NaverStreamer()
    naver.options.n_limits = 1
    naver.options.display_rank = True
    naver.options.verbose = True
    naver.stream(async=False, interval=0)


def test_result_exists():
    """Check if files are correctly created. """

    items = glob.glob(DATA_DIR+"*trend*")
    assert len(items) > 0
