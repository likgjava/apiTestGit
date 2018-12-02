import requests

# 获取验证码
url = "http://localhost/index.php?m=Home&c=User&a=verify&r=0.7585288501934007"
# url = "http://localhost/index.php?m=Home&c=User&a=verify&type=user_reg&r=0.04863238375369461"
response = requests.get(url)
print(response.cookies)
session_id = response.cookies.get("PHPSESSID")
print("session_id=", session_id)

cookies = {"PHPSESSID": session_id}
# cookies = {}

# 注册
url = "http://localhost/Home/User/reg.html?t=0.7585288501934007"
data = {"username": "13012345678", "password": "123456", "password2": "123456", "verify_code": "8888"}
response = requests.post(url, data=data, cookies=cookies)
print(response.headers)
print(response.text)

# # 登录
# url = "http://localhost/index.php?m=Home&c=User&a=do_login&t=0.7585288501934007"
# data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
# response = requests.post(url, data=data, cookies=cookies)
# print(response.headers)
# print(response.json())
#
# # 订单列表
# response = requests.get("http://localhost/Home/Order/order_list.html", cookies=cookies)
# # print(response.text)
