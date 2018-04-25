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

