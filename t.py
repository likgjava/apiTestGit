# 请写⼀段代码，向 http://httpbin.org/json 这个 API 发送⼀个 GET 请求,
# 并打印响应⾥的 title 字段的值，和 slides 字段⾥元素的个数。
# 输出格式: title: xxx, slides count: x.
# 运⾏⽰例:
# In [3]: fetch_and_parse()
# title: Simple Title, slides count: 2.

import requests
def fetch_and_parse():
    response = requests.get("http://httpbin.org/json")
    json_data = response.json()
    print(json_data)
    slideshow = json_data.get("slideshow")
    title = slideshow.get("title")
    slides = slideshow.get("slides")
    print("title: {}, slides count: {}".format(title, len(slides)))


fetch_and_parse()
