import requests

# 注册
# data = {"username": "likg", "password": "123"}
# response = requests.post("https://mock.boxuegu.com/mock/83/frame/register", data=data)
# print(response.headers)
# print(response.json())

# 登录
# data = {"username": "likg", "password": "123"}
# response = requests.post("https://mock.boxuegu.com/mock/83/frame/login", data=data)
# print(response.headers)
# print(response.json())

# 用户资料
data = {"username": "likg", "password": "123"}
response = requests.post("https://mock.boxuegu.com/mock/83/frame/profile")
print(response.headers)
print(response.json())



