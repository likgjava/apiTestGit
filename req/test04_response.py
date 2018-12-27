import requests

response = requests.get("http://www.baidu.com")

# response.status_code 状态码
print("status_code=", response.status_code)

# response.url         请求url
print("url=", response.url)

# response.encoding    查看响应头部字符编码
print("encoding=", response.encoding)

# response.headers     头信息
print("headers=", response.headers)

# response.cookies     cookie信息
print("cookies=", response.cookies)

# response.text        文本形式的响应内容
print("text=", response.text)

# response.content     字节形式的响应内容
print("content=", response.content)

# response.json()      JSON形式的响应内容
print("json=", response.json())