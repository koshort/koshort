Streamer
========

Streaming Naver trends
----------------------

Naver is a most famous Korean search engine website and they provides the most searched keywords.

..code-block:: python

    >>> from koshort.stream import NaverStreamer
    >>> streamer = NaverStreamer()
    >>> streamer.options.verbose = True  # Print streaming results.
    >>> streamer.options.display_rank = True  # Print ranking of the keywords.
    >>> streamer.n_limits = 5  # stop streaming when n amount of data gathered.
    >>> streamer.stream(interval=30)  # crawl every 30 seconds.
    cj채용
    온주완의 뮤직쇼
    유상무
    현대차
    ...

Streaming filtered tweets
-------------------------

Twitter is one of the best source to find a Korean spoken-language and short messages. (where idea of the name Koshort came from)
If you don't already have a twitter API access, please refer `here <https://apps.twitter.com/>`

..code-block:: python

    >>> import sys
    >>> import os
    >>> from koshort.stream import TwitterStreamer
    >>> # Initialize streamer with path to save data and list of words to be used in streaming.
    >>> app = TwitterStreamer("data/", ["가","나","다","라"], async=True)  # You can use out-of-the-box Threading with async=True
    >>> # Show options available
    >>> app.show_options()
    access_token = None
    access_token_secret = None
    consumer_key = None
    consumer_secret = None
    filter_retweets = False
    output_as_onefile = False
    output_extension = txt
    output_prefix = tweet
    remove_links = False
    remove_mentions = False
    tweet_limits = 1000000
    verbose = False
    >>> # Set the options you desire
    >>> # Underlining consumer key, consumer secret, access token, access token secret must be provided.
    >>> app.options.consumer_key = '' 
    >>> app.options.consumer_secret = ''
    >>> app.options.access_token = ''
    >>> app.options.access_token_secret = ''
    >>> app.options.filter_retweets=True
    >>> app.options.output_extension='twt'
    >>> app.options.output_prefix=''
    >>> app.options.remove_links=True
    >>> app.options.remove_mentions=True
    >>> app.options.tweet_limits=10
    >>> app.options.verbose=True
    >>> # Initialize application and launch it
    >>> app.create_listener()
    >>> app.stream()
    2 오늘ㄴ셤끗나면 파판안하고 그림그려야지 컴션 다 끗내고싶어 낼까지
    1  다 #더쇼 #빅스LR 투표
    2 월요일에 브레이커스에 가서 기점이를 만났어!!일도 잘하고 다 완벽해!!!!!!!!!!
    3  죠아욥 ㅠ 근데 나 돈이없어서 s나 a가 학생할인되길래 할건데 괭ㅌ찮아?
    2 나 지금 드려야할 깊티가 5개인데 월급이 안들어옴 ㅅㅂ
    4 6. 비슷 한 뜻을 가진 단어 들을 사전으로 다 열람 해 본 후 선택해서 쓰는 소소한 재미를 즐기기도 합니다. 아직 공개하지 않은 글 이지만 아주 예전부터 쓰고 싶어서 저장만 해 둔 필연 이라는 글이 있는데… 
    1  와악 나 루날님한테 물어볼 거 많을 것 같아요 ㅇ&lt;-&lt;
    2  저는 치킨은 다 좋아해요
    치느님 앞에서 감히 취향을 논하다니 그거슨 넘 건방진 것 '^'
    1  와 민현풀셋이시네요😙 저는 다 교환으로 꾸렸죠...
    1 ? 이게 다 무슨소리야 씹뽤