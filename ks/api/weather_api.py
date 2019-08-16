"""
2.使用requests库完成接口测试。（20分）
已知信息为：
城市编号数据：
101010100   北京
101020100   上海
101030100   天津
101040100   重庆
请求获取天气的接口：http://www.weather.com.cn/data/sk/101010100.html
百度查询接口：https://www.baidu.com/s?wd=北京
测试要求：
1)根据城市编号，请求获取天气的接口
2)获取返回结果中的城市名称
3)请求百度查询接口，把获取到的城市名称作为请求参数
4)把百度查询的返回数据保存到MySQL数据库中
5)要求对提供的所有城市编号数据进行测试，并实现参数化
"""
import requests


class WeatherApi:
    def __init__(self):
        self.weather_url = "http://www.weather.com.cn/data/sk/{}.html"

    def query_weather(self, city_code):
        url = self.weather_url.format(city_code)
        return requests.get(url)
