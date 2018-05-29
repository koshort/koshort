# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime

def convert_utf8_to_euckr(unicode_string):
    return unicode_string.encode('euc-kr', 'replace').decode('euc-kr')

def get_trendlist_of_date(trend_data, target_date='yyyymmdd'):
    trends_list = trend_data['default']['trendingSearchesDays']
    for trend in trends_list:
        if(trend['date'] == target_date):
            return trend['trendingSearches']

    return trends_list[0]['trendingSearches'] # default, most recently


url = "https://trends.google.com/trends/api/dailytrends"
querystring = {"hl":"ko","geo":"KR"}
response = requests.request("GET", url, params=querystring)

### 데이터 전처리부분
text = response.content.decode('unicode_escape')
# 첫줄이')]}\',와 같은 의미없는 문자가 들어있어서 제외
text = text.split('\n')[1]
text = convert_utf8_to_euckr(text)
data = json.loads(text)

today_time = datetime.today().strftime("%Y%m%d")
current_trendlist = get_trendlist_of_date(data, today_time)

current_trendlist = [(trend['title']['query'], trend['formattedTraffic']) for trend in current_trendlist]


print(current_trendlist)
# print(data['default']['trendingSearchesDays'][0]['trendingSearches'][1]['title']['query'])
# pprint.pprint(data)
