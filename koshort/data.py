from __future__ import absolute_import
from koshort.constants import DATA_DIR
import os


def clear():
    """clear the koshort output data directory

    .. code-block:: python

        >>> import koshort
        >>> koshort.clear()

    """

    items = os.listdir(DATA_DIR)
    for item in items:
        os.remove(item)


class StringWriter(object):
    def __init__(self, filename):
        self.writer = open(DATA_DIR+filename, mode='a', encoding='utf-8')

    def write(self, string):
        self.writer.write(string)
        self.writer.write('\n')
