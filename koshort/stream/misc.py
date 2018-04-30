from time import sleep
from koshort.stream import BaseStreamer, TwitterStreamer
from koshort.stream.naver import get_current_trend


class NavtterStreamer(BaseStreamer):
    """Start streaming of twitter about naver's top trending keywords. 

    ..code-block:: python

        >>> from koshort.stream import NavtterStreamer
        >>> streamer = NavtterStreamer()
        >>> streamer.naver.

    """

    def __init__(self):
        parser = self.get_parser()
        parser.add_argument(
            '-i', '--interval', 
            help="streaming interval(secs)", 
            default=100,
            type=int
        )
        self.options, _ = parser.parse_known_args()
        self.twitter  = TwitterStreamer()
        self.trend = None
        self.streamer = None

    def get_trend(self):
        _, self.trend = get_current_trend()
        if self.options.verbose:
            print(self.trend)

    def job(self):
        self.get_trend()
        twitter = TwitterStreamer(word_list=self.trend, async=False)
        twitter.options = self.twitter.options
        twitter.options.time_limits = self.options.interval
        twitter.create_listener()
        twitter.job()
        self.job()
