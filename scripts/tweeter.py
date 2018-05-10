from koshort.stream import TwitterStreamer

app = TwitterStreamer(async=False)
app.options.verbose = True
app.show_options()
app.create_listener()
app.stream(async=False)