# 1). 访问查询天气信息的接口，并获取JSON响应数据
# 2). 接口地址：http://www.weather.com.cn/data/sk/101010100.html

# 1.导包
import requests

# 2.发送请求
response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")
# response = requests.get("http://www.baidu.com")
print("encoding=", response.encoding)
response.encoding = "UTF-8"
print("encoding=", response.encoding)
# 3.获取响应数据
json_data = response.json()

print("encoding=", response.encoding)
print("data type=", type(json_data))
print("json_data=", json_data)

