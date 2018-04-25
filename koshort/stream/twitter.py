# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import tweepy
import urllib3
import re
import sys

if int(sys.version[0]) > 2:
    import configparser
else:
    import ConfigParser as configparser

from argparse import ArgumentParser


__all__ = ['TwitterStreamer']


class CorpusListener(tweepy.StreamListener):
    def __init__(self, args, cfg, dirname, word_list):
        """CorpusListener is a tweepy listener to listen on filtered list of words.
        
        Args:
            args (object): arg parser argument object
            cfg (object): config parser object
            dirname (str): string of directory
            word_list (list): list of words
        """

        # WARNING: This underlining keys and tokens 
        # should not be shared or uploaded on any public code repository!
        self.consumer_key = cfg.get('api', 'consumer_key')
        self.consumer_secret = cfg.get('api', 'consumer_secret')
        self.access_token = cfg.get('api', 'access_token')
        self.access_token_secret = cfg.get('api', 'access_token_secret')

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

        self.dirname = dirname
        self.words = word_list
        self.args = args

        self.limit = 0

    @staticmethod
    def delete_links(tweet):
        return re.sub(r'http\S+', '', tweet)
    
    @staticmethod
    def delete_mentions(tweet):
        return re.sub(r'@\S+', '', tweet)

    def on_status(self, status):
        tweet = status.text

        # Except potentially repetitive retweets
        def write_tweets_to_files(tweet):
            if self.args.remove_links:
                tweet = self.delete_links(tweet)
            if self.args.remove_mentions:
                tweet = self.delete_mentions(tweet)

            word_count = 0

            if not self.args.output_as_onefile:
                # counts how many targeting words included in one tweet.
                for word in self.words:
                    word_count += tweet.count(word)

            filename = "{}{}{}.{}".format(
                self.dirname,
                self.args.output_prefix,
                word_count,
                self.args.output_extension
                )

            n_word_file = open(filename, 'a', encoding='utf-8')
            n_word_file.write(tweet)
            n_word_file.write("\n")

            if self.args.verbose:
                print(word_count, tweet)

            self.limit += 1

        if self.args.filter_retweets:
            if not "RT @" in tweet:
                write_tweets_to_files(tweet)
        else:
            write_tweets_to_files(tweet)

        if self.limit == self.args.tweet_limits:
            return "Done"

    def on_error(self, status_code):
        if status_code == 420:  # if connection failed
            return False


def get_parser():
    """customized argument parser to set various parameters for SegEngine

    Returns:
        object: argument parser.
    """

    p = ArgumentParser()
    p.add_argument(
        '-v', '--verbose', 
        help="increase verbosity", 
        action="store_true"
    )
    p.add_argument(
        '-c', '--config_file', 
        help='path to ini format configuration file',
        type=str
    )
    p.add_argument(
        '--filter_retweets', 
        help='do not save potentially repetitive retweets',
        action="store_true",
    )
    p.add_argument(
        '--remove_links', 
        help='remove links included into each tweet',
        action="store_true",
    )
    p.add_argument(
        '--remove_mentions', 
        help='remove mentions included into each tweet',
        action="store_true",
    )
    p.add_argument(
        '--output_prefix', 
        help='prefix of the output file',
        default='tweet',
        type=str
    )
    p.add_argument(
        '--output_as_onefile', 
        help='save output as onefile',
        action="store_true",
    )
    p.add_argument(
        '--output_extension', 
        help='extension of the output file',
        default='txt',
        type=str
    )
    p.add_argument(
        '--tweet_limits', 
        help='stop when this amount of tweets are collected',
        default=1000000,
        type=int
    )
    return p


class TwitterStreamer(object):
    """Start streaming on Twitter with your api keys and tokens.

    Args:
        dirname (str): directory to save output files.
        word_list (list): list of words to be streamed.
    """
    def __init__(self, dirname, word_list):
        parser = get_parser()
        args = parser.parse_args()
        cfg = configparser.ConfigParser()
        cfg.read(args.config_file)
        listener = CorpusListener(args, cfg, dirname, word_list)
        api = listener.api

        self.dirname = dirname
        self.word_list = word_list
        self.streamer = tweepy.Stream(auth=api.auth, listener=listener)

    def run(self):
        """Try to stream recursively when it fails due to protocol error. """
        try:
            self.streamer.filter(track=self.word_list, async=True)
        except urllib3.exceptions.ProtocolError:
            self.run()
