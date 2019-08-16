# 访问百度的搜索接口，通过查询字符串的方式传递搜索的关键字python，并查看响应数据
# 请求路径格式为：http://www.baidu.com/s?wd=python

# 1.导包
import requests

# 2.发送请求
# response = requests.get("http://www.baidu.com/s?wd=python")
# response = requests.get("http://www.baidu.com/s", params="wd=python")

response = requests.get("http://www.baidu.com/s", params={"wd": "python", "name": "tom"})

# 3.获取响应结果
print("text=", response.text)
print("url=", response.url)
