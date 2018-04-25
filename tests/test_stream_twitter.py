"""
Since continuous integration testing is limited 
due to API keys and token's publicity issue, additional local tests are needed.
"""

import subprocess
import time
import glob
import os
import koshort
from koshort.constants import DATA_DIR


def test_twitter_streamer():
    from koshort.stream import TwitterStreamer

def test_clear_data():
    """Check if file is correctly cleared."""

    koshort.clear()
    items = glob.glob(DATA_DIR+"*")
    assert len(items) == 0