# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from argparse import ArgumentParser


class BaseStreamer(object):
    def get_parser(self):
        """customized argument parser to set various parameters

        Returns:
            object: argument parser.
        """

        parser = ArgumentParser()
        parser.add_argument(
            '-v', '--verbose', 
            help="increase verbosity", 
            action="store_true"
        )
        return parser

    def show_options(self):
        """Print out options available and predefined values."""

        for attr, value in sorted(vars(self.options).items()):
            print("{} = {}".format(attr, value))