import requests

# 发送POST请求
# response = requests.post("http://www.baidu.com", data={"username": "tom", "pwd": "123"})
response = requests.post("http://www.baidu.com", json={"username": "tom", "pwd": "123"})

# 获取响应内容
print("text=", response.text)
