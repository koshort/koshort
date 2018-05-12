from koshort.stream import NaverStreamer


def main():
    app = NaverStreamer(is_async=False)
    app.options.verbose = True
    app.show_options()
    app.stream()


if __name__ == '__main__':
    main()