from koshort.stream import NaverStreamer, TwitterStreamer, BaseStreamer


class InteractiveStreamer(BaseStreamer):
    """Interactively combine two streamers to stream correlated data."""

    def __init__(self):
        parser = self.get_parser()
        parser.add_argument(
            '-i', '--interval', 
            help="streaming interval(secs)", 
            type=int
        )
        self.options, _ = parser.parse_known_args()
        self.naver = NaverStreamer()
        self.twitter = TwitterStreamer()
        self.trend = None

    def get_trend(self):
        self.trend = self.naver.get_current_trend()
