# 导包
import requests

# 发送GET请求
response = requests.get("http://www.baidu.com")

# 获取响应内容
print("text=", response.text)







