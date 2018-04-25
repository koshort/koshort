from __future__ import absolute_import
from koshort.constants import DATA_DIR
import os
import glob


def clear():
    """clear the koshort data directory

    .. code-block:: python

        >>> import koshort
        >>> koshort.clear()

    """

    items = glob.glob(DATA_DIR+"/*")
    for item in items:
        os.remove(item)