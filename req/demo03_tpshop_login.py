import requests

# 获取验证码
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(response.cookies)
cookie_data = {"PHPSESSID": response.cookies.get("PHPSESSID")}
print("-----------------------------")

# 登录
login_data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
response = requests.post("http://localhost/index.php?m=Home&c=User&a=do_login", data=login_data, cookies=cookie_data)
print(response.cookies)
print("login response data=", response.json())
print("-----------------------------")

# 我的订单
response = requests.get("http://localhost/Home/Order/order_list.html", cookies=cookie_data)
print(response.text)
