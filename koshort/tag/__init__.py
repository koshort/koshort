try:
    from koshort.tag._mecab import Mecab
except (ModuleNotFoundError, ImportError) as e:
    print("Install either mecab-python or mecab-python-windows in order to use mecab tagging. you can easily install one of them with :pip install mecab-python")