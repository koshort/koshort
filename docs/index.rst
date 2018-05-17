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

For step-by-step instructions, follow the :doc:`tutorial <streamer>` and explore :doc:`examples <examples>`.
For specific descriptions of each module, go see the :ref:`api` documents.

Lowering the barrier to the domain-specific internet corpus
-----------------------------------------------------------

Social network services and other internet communities are open and rich data source of human spoken language.
But due to the issues of privacy and policy of each website, sharing a bunch of retrieved text data is normally prohibited.
To solve the most major Natural Language Processing (NLP) problem under this circumstances, researchers had to rely on limited public datasets and data brought by their company.
Otherwise they would implement their domain-specific crawler for each case.

Koshort is hardly inspired by the project `KoNLPy <http://konlpy.org>`_, with similar philosophy. It is not about recreating another crawler but to unify efforts around so that anyone can accelerate their projects.

Use out-of-box script

.. code-block:: python

    > stream_naver
    display_rank = False
    filename = trends.txt
    interval = 60
    n_limits = 10
    verbose = True
    시크릿 마더
    무법변호사
    신아영
    미얀마
    로드fc
    소진
    위너
    불후의명곡
    그것이 알고싶다
    짠내투어
    아는형님
    로또
    로또806회
    msi
    전지적 참견 시점
    김재훈
    아이돌룸
    토익
    아오르꺼러
    같이 살래요


Use koshort API

.. code-block:: python

    >>> from koshort.stream import NaverStreamer
    >>> streamer = NaverStreamer()
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


Contribute
----------

Koshort is just another newly created library.
It can continuously evolve and we need your help!

Found a bug? Do you have a good idea for improving koshort?
Visit `Koshort GitHub page <https://github.com/koshort/koshort>`_
and `suggest an idea <https://github.com/koshort/koshort/issues>`_
or `make a pull request <https://github.com/koshort/koshort/pulls>`_.

You are also welcome to join
our `discord <https://discord.gg/eNFUnZt>`_

Please note that
*asking questions through these channels is also a great contribution*,
Because it gives the community feedback as well as ideas.
Please don't hesitate to ask.


User guide
----------

.. toctree::
  :glob:
  :maxdepth: 2

  streamer
  examples

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
