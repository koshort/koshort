"""
Koshort is a Python package for Korean internet trends streaming and processing… or maybe abbreviation of Korean domestic cat.

Koshort uses ./data as a default data directory to save crawled results.
You can use following tricks when you use them.

.. code-block:: python

    >>> import koshort
    >>> koshort.clear()  # Delete every file in data directory.
    >>> koshort.listdir()  # Show what's in data directory.

"""
from __future__ import absolute_import

import pkg_resources

from koshort.about import *
from koshort.data import clear, listdir
from koshort import stream  # Subpackage pre-loading
