"""
Koshort is a Python package for Korean internet trends streaming and processing… or maybe abbreviation of Korean domestic cat.

Koshort uses ./data as a default data directory to save crawled results.
You can use following tricks when you use them.

..code-block:: python

    >>> import koshort
    >>> koshort.clear()  # Delete every file in data directory.
    >>> koshort.listdir()  # Show what's in data directory.

"""

import pkg_resources

__title__ = 'koshort'
__author__ = 'nyanye'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2018 Nyanye'

try:
    __version__ = pkg_resources.get_distribution('koshort').version
except pkg_resources.DistributionNotFound:
    __version__ = "dev"

from koshort.data import clear, listdir
from koshort import stream, tag  # Subpackage pre-loading