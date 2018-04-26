# -*- coding: utf-8 -*-

import os
import sys
from setuptools import find_packages, setup

__version__ = '0.3.9.3'

def requirements():
    def _openreq(reqfile):
        with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
            return f.read().splitlines()

    if sys.version_info >= (3, ):
        return _openreq('requirements.txt')
    else:
        return _openreq('requirements.txt')
        # raise Exception("Koshort does not support python2.* distribution.")  # This is final decision to deprecate 2.* if needed..

setup(
    name='koshort',
    version=__version__,
    description='Python package for Korean natural language processing.',
    url='http://koshort.readthedocs.io',
    author='nyanye',
    author_email='iam@nyanye.com',
    keywords=['Korean', 'CJK',
              'NLP', 'natural language processing',
              'CL', 'computational linguistics',
              'tagging', 'tokenizing', 'linguistics', 'text analytics'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        ],
    license='GPL v3+',
    packages=find_packages(),
    install_requires=requirements())