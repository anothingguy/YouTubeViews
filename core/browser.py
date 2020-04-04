import http.cookiejar
import mechanize
import random

from string import ascii_letters
from time import sleep

# from subprocess import call
# from platform import system
# cls = 'cls' if system() == 'Windows' else 'clear'


class Browser(object):

    def __init__(self):
        self.progresses = {}
        super(Browser, self).__init__()

    def createBrowser(self):
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_refresh(False)
        br.set_cookiejar(http.cookiejar.LWPCookieJar())
        br.addheaders = [('User-agent', self.useragent())]
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        return br

    def watch(self, url):
        if not self.alive:
            return

        try:
            br = self.createBrowser()
            if not br.open(url, timeout=5.0).read():return

            sleepTime = random.randint(self.min, self.max)
            # [sleep(1) for _ in range(sleepTime) if self.alive] # watching the video
            if self.alive:  # watching the video
                count_time = 0
                for _ in range(sleepTime):
                    count_time += 1
                    # call([cls])
                    # print('\033[32m %s/%s \033[0m' % (count_time, sleepTime))
                    self.progresses[url] = [count_time, sleepTime]
                    sleep(1)

            # search for something random
            br.select_form(id='search-form')
            br.form['search_query'] = random.choice([_ for _ in ascii_letters])

            sleep(0.5)
            br.submit()
            br.close()
            return True
        except:return

    def useragent(self):
        useragents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'
        ]
        return random.choice(useragents)
