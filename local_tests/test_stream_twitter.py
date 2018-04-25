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
    """Test twitter streamer with subprocess system call. """

    command = "python stream_twitter.py -c config/stream_dev.ini -v --filter_retweets --remove_links --remove_mentions"
    command_list = command.split()
    p = subprocess.Popen(command_list)
    time.sleep(5)
    p.kill()


def test_result_exists():
    """Check if files are created. """

    items = glob.glob(DATA_DIR+"*")
    assert len(items) > 0


def test_clear_data():
    """Check if file is correctly cleared."""

    koshort.clear()
    items = glob.glob(DATA_DIR+"*")
    assert len(items) == 0