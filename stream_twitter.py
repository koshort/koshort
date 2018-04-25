from koshort.stream import TwitterStreamer

if __name__ == '__main__':
    app = TwitterStreamer("data/", ["그냥", "오늘", "치킨이", "먹고싶다"])
    app.run()
