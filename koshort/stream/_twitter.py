# -*- coding: utf-8 -*-
import tweepy
import urllib3
import re
import sys
if int(sys.version[0]) > 2:
    import configparser
else:
    import ConfigParser as configparser
from argparse import ArgumentParser


class CorpusListener(tweepy.StreamListener):
    """CorpusListener is a tweepy listener to listen on filtered list of words.
    """

    def __init__(self, args, cfg, dirname, word_list):
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

    def on_status(self, status):
        data_str = status.text

        # Except potentially repetitive retweets
        if not "RT @" in data_str:
            data_str = re.sub(r'http\S+', '', data_str)  # Delete links
            data_str = re.sub(r'@\S+', '', data_str)  # Delete mentions
            count = 0

            # counts how many targeting words included in one tweet.
            for word in self.words:
                count += data_str.count(word)

            n_word_file = open(self.dirname+str(count)+'.'+self.args.output_extension, 'a', encoding='utf-8')
            n_word_file.write(data_str)
            n_word_file.write("\n")

            if self.args.verbose:
                print(count, data_str)

            self.limit += 1

        if self.limit == 1000000:
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
        '--output_extension', 
        help='extension of the output file',
        default='txt',
        type=str
    )
    return p


def stream_twitter(dirname, word_list):
    args = get_parser().parse_args()
    cfg = configparser.ConfigParser()
    cfg.read(args.config_file)
    listener = CorpusListener(args, cfg, dirname, word_list)
    api = listener.api
    streamer = tweepy.Stream(auth=api.auth, listener=listener)
    try:
        streamer.filter(track=word_list, async=True)
    except urllib3.exceptions.ProtocolError:
        stream_twitter(dirname, word_list)
