# 请求IHRM项目的登录接口，URL：http://182.92.81.159/api/sys/login
# 请求头：Content-Type: application/json
# 请求体：{"mobile":"13800000002", "password":"123456"}


# 1.导包
import requests

# 2.发送请求
url = "http://182.92.81.159/api/sys/login"
data = '{"mobile":"13800000002", "password":"123456"}'
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=data, headers=headers)

# response = requests.post(url, json={"mobile":"13800000002", "password":"123456"})

# 3.获取响应数据
print("json data=", response.json())
