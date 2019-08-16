# 1.导包
import requests

# 2.发送请求
response = requests.get("http://www.baidu.com")

# 3.获取响应数据
# 1). 访问百度首页的接口`http://www.baidu.com`，获取以下响应数据
# 2). 获取响应状态码
print("status_code=", response.status_code)

# 3). 获取请求URL
print("url=", response.url)

# 4). 获取响应字符编码
print("encoding=", response.encoding)

# 5). 获取响应头数据
print("headers=", response.headers)

# 6). 获取响应的cookie数据
print("cookie=", response.cookies)

# 7). 获取文本形式的响应内容
print("text=", response.text)

# 8). 获取字节形式的响应内容
print("content=", response.content)
