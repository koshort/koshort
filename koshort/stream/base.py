# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from argparse import ArgumentParser
from koshort.threading import PropagatingThread
import urllib3


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

    def stream(self, async=True):
        try:
            if async:
                    self._thread = PropagatingThread(target=self.job)
                    self._thread.start()
                    self._thread.join()
            else:
                self.job()
        except urllib3.exceptions.ProtocolError:
            print("ProtocolError has raised but continue to stream.")
            self.stream(async=async)
        except RecursionError:
            return False
        except KeyboardInterrupt:
            print("User has interrupted.")
            return False