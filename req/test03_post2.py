# 请求IHRM项目的登录接口，请求数据（{"mobile":"13800000002", "password":"123456"}）
# 登录接口URL：http://182.92.81.159/api/sys/login

# 1.导包
import requests

# 2.发送POST请求
url = "http://182.92.81.159/api/sys/login"
data = {"mobile": "13800000002", "password": "123456"}
response = requests.post(url, json=data)

# 3.获取响应数据
print("text=", response.text)
print("json data=", response.json())
