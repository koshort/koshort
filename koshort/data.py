from __future__ import absolute_import
from koshort.constants import DATA_DIR
import os
import glob


def clear():
    """clear the koshort output data directory

    .. code-block:: python
        >>> import koshort
        >>> koshort.clear()

    """

    items = glob.glob(DATA_DIR+"*")
    for item in items:
        os.remove(item)


def listdir():
    """list koshort default data directory.

    .. code-block:: python
        >>> import koshort
        >>> koshort.listdir()
    
    """

    print(os.listdir(DATA_DIR))


class CorpusReader(object):
    def __init__(self, extension='.txt'):
        """CorpusReader reads corpuses in koshort data directory.
            extension (str, optional): Defaults to '.txt'. extension of corpus to load.

        .. code-block:: python
            >>> from koshort.data import CorpusReader
            >>> reader = CorpusReader()
            >>> reader.read()
            >>> reader.corpus
            {...}
            >>> reader.items = ["data/specific_corpus.txt"]
            >>> reader.read()
            >>> reader.corpus['specific_corpus.txt']
            content of corpus
        """

        self.items = glob.glob(DATA_DIR+"*"+extension)
        self.corpus = {}

    def read(self):
        """read method reads all files included 
        in items attr and save it into corpus dictionary.
        """

        for filename in self.items:
            reader = open(filename, mode='r+', encoding='utf-8')
            self.corpus[os.path.basename(filename)] = reader.read()


class StringWriter(object):
    def __init__(self, filename):
        self.writer = open(DATA_DIR+filename, mode='a', encoding='utf-8')

    def write(self, string):
        self.writer.write(string)
        self.writer.write('\n')
