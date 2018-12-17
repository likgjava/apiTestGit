import requests

response = requests.get("http://www.baidu.com", cookies={"c1": "v1"})
print(response.cookies)
print(response.cookies["BDORZ"])
print(len(response.cookies))
# print(response.text)
print("-----------------------------")

response = requests.get("http://localhost")
print(response.cookies)
