import requests


class BaiduApi:
    def __init__(self):
        self.baidu_url = "http://www.baidu.com/s?wd={}"

    def search_kw(self, kw):
        url = self.baidu_url.format(kw)
        print("url=", url)
        return requests.get(url)
