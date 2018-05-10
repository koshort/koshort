# -*- coding: utf-8 -*-

import os
import sys
from setuptools import find_packages, setup

__version__ = '0.3.9.5'

def requirements():
    def _openreq(reqfile):
        with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
            return f.read().splitlines()

    if sys.version_info >= (3, ):
        return _openreq('requirements.txt')
    else:
        raise Exception("Koshort does not support python2.* distribution.")  # This is final decision to deprecate 2.* if needed..

setup(
    name='koshort',
    version=__version__,
    description='koshort is a Python package for Korean internet spoken language crawling and processing... or maybe Korean domestic cat.',
    long_description="""\
Social network services and other internet communities are open and rich data source of human spoken language.
But due to the issues of privacy and policy of the each websites, sharing bunch of retrieved text data is normally prohibited.
To solve the most major Natural Language Processing (NLP) problem under this circumstances, researchers had to rely on limited public datasets and data brought by their company.
Otherwise they would implement their domain specific crawler for each cases.

Koshort is hardly inspired by the project KoNLPy, with similar philosphy. It is not about recreating another crawler but to unify efforts around so that anyone can accelerate their projects.
        """,
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
    entry_points={
        'console_scripts': [
            'stream_twitter = koshort.__scripts__.tweeter:main'
        ],
    },
    license='GPL v3+',
    packages=find_packages(),
    install_requires=requirements())