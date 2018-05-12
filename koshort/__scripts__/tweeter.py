from koshort.stream import TwitterStreamer


def main():
    app = TwitterStreamer(is_async=False)
    app.options.verbose = True
    app.show_options()
    app.create_listener()
    app.stream()


if __name__ == '__main__':
    main()