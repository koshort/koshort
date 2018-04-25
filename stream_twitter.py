from koshort.stream import TwitterStreamer

if __name__ == '__main__':
    app = TwitterStreamer("data/", ["가","나","다","라"])
    # app.args.remove_links = True
    # app.args.remove_mentions = True
    # app.args.verbose = True
    # app.args.tweet_limits = 1000
    app.create_listener()
    app.run()
