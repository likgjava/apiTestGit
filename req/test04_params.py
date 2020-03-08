import requests

# 方式一：直接定义在URL中
# response = requests.get("http://localhost/Home/Goods/search.html?q=iPhone")

# 方式二：传递字符串方式的参数
# response = requests.get("http://localhost/Home/Goods/search.html", params="q=iPhone")

# 方式三：传递字典类型的参数
response = requests.get("http://localhost/Home/Goods/search.html", params={"q": "iPhone"})

# 获取响应结果
print("url=", response.url)
