# 1. 导包
import requests

# 2. 调用requests库的API发送请求，发送GET请求
response = requests.get("http://www.baidu.com")

# 3. 获取响应数据
print("text=", response.text)
