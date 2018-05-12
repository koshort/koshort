from __future__ import absolute_import

try:
    from koshort.tag._mecab import Mecab
except:  # ImportError and ModuleNotFoundError from python3.5+ is expected.
    print("Install either mecab-python or mecab-python-windows in order to use mecab tagging. you can easily install one of them with :pip install mecab-python")