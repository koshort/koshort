.. koshort documentation master file, created by
   sphinx-quickstart on Wed Apr 25 18:43:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Koshort: Korean trends streaming in python
==========================================

.. image:: https://travis-ci.org/koshort/koshort.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/koshort/koshort

.. image:: https://readthedocs.org/projects/koshort/badge/?version=latest
    :alt: Documentation Status
    :target: http://koshort.readthedocs.io/en/latest/?badge=latest

Koshort is a Python package for Korean internet trends streaming and processing... or maybe abbreviation of Korean domestic cat.

For step-by-step instructions, follow the :ref:`guide`.
For specific descriptions of each module, go see the api documents.

.. sourcecode:: python

    # Install koshort
    git clone https://github.com/koshort/koshort.git
    cd koshort

    # python
    >>> from koshort.stream import naver
    >>> streamer = naver.NaverStreamer()
    >>> streamer.stream()
    cj채용
    온주완의 뮤직쇼
    유상무
    현대차
    ...


License
-------

Koshort is Open Source Software, and is released under the license below:

- `GPL v3 or above <http://gnu.org/licenses/gpl.html>`_

API
---

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   koshort


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
