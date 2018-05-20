<br><br>

<h1 align="center">Koshort</h1>

<p align="center">
  <a href="/LICENSE"><img src="https://img.shields.io/badge/License-GPL%20v3-blue.svg"/></a>
  <a href="https://travis-ci.org/koshort/koshort"><img src="https://travis-ci.org/koshort/koshort.svg?branch=master"/></a>
  <a href="https://koshort.readthedocs.io/"><img src="https://readthedocs.org/projects/koshort/badge/?version=latest" /></a>
  <a href="https://pypi.org/project/koshort/"><img src="https://badge.fury.io/py/koshort.svg" /></a>
  <a href="https://discord.gg/eNFUnZt"><img src="https://img.shields.io/badge/chat-discord-ff69b4.svg" /></a>  
</p>

<p align="center">
    한국어 인터넷 트렌드 스트리밍과 처리를 위하여 만들어진 파이썬 패키지 코숏<br>
    koshort is a Python package for Korean internet trends streaming and processing... or maybe Korean domestic cat :cat:
</p>

<br><br><br>

* English Documentation: [http://koshort.readthedocs.io/](http://koshort.readthedocs.io/)
* 한국어 문서: [http://koshort.readthedocs.io/ko/latest/](http://koshort.readthedocs.io/ko/latest)

## Installation
The easiest way to install the latest version is by using pip/easy_install to pull it from PyPI:

```bash
pip install koshort
```

You may also use Git to clone the repository from GitHub and install it manually:

```bash
git clone https://github.com/koshort/koshort.git
cd koshort
python setup.py install
```

Python 3.3, 3.4, 3.5 & 3.6 are supported.  
3.7 compatibility soon will be available.

## Examples
Use out-of-box script
```shell
$ stream_naver
display_rank = False
filename = trends.txt
interval = 60
n_limits = 10
verbose = True
시크릿 마더
무법변호사
신아영
미얀마
로드fc
소진
위너
불후의명곡
그것이 알고싶다
짠내투어
아는형님
로또
로또806회
msi
전지적 참견 시점
김재훈
아이돌룸
토익
아오르꺼러
같이 살래요
```
Use koshort API
```shell
$ python
>>> from koshort.stream import naver
>>> streamer = naver.NaverStreamer()
>>> streamer.stream()
cj채용
온주완의 뮤직쇼
유상무
현대차
...
```

## Copyright
copyright by 2018 Nyanye with :purple_heart:
