from datetime import datetime
from bs4 import BeautifulSoup, SoupStrainer
from koshort.stream import BaseStreamer

import requests
import time
from pprint import pprint


class DCInsideStreamer(BaseStreamer):
    """DCInside is a biggest community website in Korea.
    DCInsideStreamer helps to stream specific gallery from past to future.
    """

    def __init__(self, markup='lxml', is_async=True):
        self.is_async = is_async

        parser = self.get_parser()
        parser.add_argument(
            '--include_comments',
            help='include comments',
            action='store_true'
        )
        parser.add_argument(
            '--comments_per_page',
            help='comments per page to be crawled',
            default=40,
            type=int
        )
        parser.add_argument(
            '--gallery_id',
            help='specify gallery id such as: cat, dog',
            default='cat',
            type=str
        )
        parser.add_argument(
            '--init_post_id',
            help='initial post_id to start crawling',
            default=0,
            type=int
        )
        parser.add_argument(
            '--final_post_id',
            help='final post_id to stop crawling',
            default=10000,
            type=int
        )
        parser.add_argument(
            '--forever',
            help='try crawling for forever',
            action='store_true'
        )
        parser.add_argument(
            '--timeout',
            help='crawling timeout per request',
            default=5,
            type=float
        )
        parser.add_argument(
            '--interval',
            help='crawling interval per request to prevent blocking',
            default=0.5,
            type=float
        )
        # TODO: Add include_metadata

        self.options, _ = parser.parse_known_args()
        self._session = requests.Session()
        self._markup = markup
        self._view_url = 'http://gall.dcinside.com/board/view'
        self._current_post_id = self.options.init_post_id
        self._done = False
    
        self._strainer = SoupStrainer('div', attrs={'class': [
            're_gall_top_1',    # 제목, 글쓴이, 작성시각
            'btn_recommend',    # 추천, 비추천
            'gallery_re_title', # 댓글
            's_write',          # 본문
        ]})

    def get_post(self, gallery_id, post_no):
        try:
            # Custom header is required in order to request.
            header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

            # Site's anti-bot policy may block crawling
            time.sleep(self.options.interval)
            r = self._session.get('%s/?id=%s&no=%d' % (self._view_url, gallery_id, post_no),
                                headers=header, timeout=self.options.timeout)

            post = self.parse_post(r.text, 'lxml', self._strainer)
            post['gallery_id'] = gallery_id
            post['post_no'] = post_no
            post['crawled_at'] = datetime.now().isoformat()

            if self.options.include_comments and post.get('comment_cnt'):
                post['comments'] = self.get_all_comments(gallery_id, post_no, post['comment_cnt'])
            return post

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            # if timeout occurs, retry
            return self.get_post(gallery_id, post_no)

        except NoSuchGalleryError:
            return self.get_post(gallery_id, post_no)

    def get_all_comments(self, gallery_id, post_no, comment_cnt):
        comment_page_cnt = (comment_cnt - 1) // self.options.comments_per_page + 1
        comments = []
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {'ci_t': self._session.cookies['ci_c'], 'id': gallery_id, 'no': post_no}

        for i in range(comment_page_cnt):
            data['comment_page'] = i + 1

            r = self._session.post('http://gall.dcinside.com/comment/view', headers=headers, data=data)
            batch = self.parse_comments(r.text)

            if not batch:
                break

            comments = batch + comments

        return comments

    def job(self):
        while not self._done:
            if self.options.final_post_id > self._current_post_id:
                result = self.get_post(self.options.gallery_id, self._current_post_id)
                if self.options.verbose:
                    pprint(result)
            else:
                self._done = True

            if self.options.forever:
                self._done = False
            
            self._current_post_id += 1

    @staticmethod
    def parse_post(markup, parser, strainer):
        soup = BeautifulSoup(markup, parser, parse_only=strainer)

        if not str(soup):
            soup = BeautifulSoup(markup, parser)

            if '/error/deleted/' in str(soup):
                return {'deleted': True}
            elif '해당 갤러리는 존재하지 않습니다' in str(soup):
                raise NoSuchGalleryError
            else:
                pass

        temp_info = soup.find(attrs={'class': 'w_top_right'})
        timestamp = temp_info.find('b').getText()

        user_info = soup.find(attrs={'class': 'user_layer'})
        user_id = user_info['user_id']
        user_ip = '' if user_id else temp_info.find(attrs={'class': 'li_ip'}).string
        nickname = user_info['user_name']

        title = soup.find('dl', attrs={'class': 'wt_subject'}).find('dd').getText()
        view_cnt = int(soup.find('dd', attrs={'class': 'dd_num'}).string)
        view_up = int(soup.find(id='recommend_view_up').string)
        view_dn = int(soup.find(id='recommend_view_down').string)
        comment_cnt = int(soup.find(id='re_count').string)
        body = str(soup.find('div', attrs={'class': 's_write'}).find('td'))

        post = {
            'user_id': user_id,
            'user_ip': user_ip,
            'nickname': nickname,

            'title': title,
            'written_at': timestamp,

            'view_up': view_up,
            'view_dn': view_dn,
            'view_cnt': view_cnt,
            'comment_cnt': comment_cnt,
            'body': body,
        }

        return post


    @staticmethod
    def parse_comments(text):
        comments = []
        soup = BeautifulSoup(text, 'lxml')
        comment_elements = soup.find_all('tr', class_='reply_line')

        for element in comment_elements:
            user_layer = element.find('td', class_='user_layer')
            nickname = user_layer['user_name']
            user_id = user_layer['user_id']
            body = element.find('td', class_='reply')
            user_ip = '' if user_id else body.find('span').extract().text
            timestamp = element.find('td', class_='retime').text

            comment = {
                'user_id': user_id,
                'user_ip': user_ip,
                'nickname': nickname,
                'written_at': timestamp,
                'body': body.text.strip()
            }

            comments.append(comment)

        return comments


class NoSuchGalleryError(Exception):
    pass


def main():
    app = DCInsideStreamer(is_async=False)
    app.options.verbose = True
    app.stream()


if __name__ == "__main__":
    main()