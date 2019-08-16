import unittest

import pymysql

from ks.api.baidu_api import BaiduApi
from ks.api.weather_api import WeatherApi
from parameterized import parameterized


def build_data():
    test_data = [("101010100", "北京"), ("101020100", "上海"), ("101030100", "天津"), ("101040100", "重庆")]
    return test_data


class Test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.weather_api = WeatherApi()
        cls.baidu_api = BaiduApi()

    def setUp(self):
        print("-" * 50)

    @parameterized.expand(build_data)
    def test01_query_weather(self, city_code, city_name):
        print("param city_code={} city_name={}".format(city_code, city_name))

        # 查询天气数据
        response = self.weather_api.query_weather(city_code)
        response.encoding = "utf-8"
        print(response.encoding)
        weather_data = response.json()
        print("weather_data=", weather_data)
        city = weather_data.get("weatherinfo").get("city")
        self.assertEqual(city_name, city)

        # 查询百度
        response = self.baidu_api.search_kw(city)
        page_source = response.text
        print("page_source=", page_source)

        # 保存到数据库
        conn = pymysql.connect("localhost", "root", "root", "test", autocommit=True)
        cursor = conn.cursor()
        sql = "insert into t_html(page_source) values('{}')".format(page_source)
        cursor.execute(sql)
        cursor.close()
        conn.close()
