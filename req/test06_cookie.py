import requests

# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print("cookies=", response.cookies)
PHPSESSID = response.cookies.get("PHPSESSID")
print("PHPSESSID=", PHPSESSID)
cookie_data = {"PHPSESSID": PHPSESSID}

# 登录：http://localhost/index.php?m=Home&c=User&a=do_login
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
response = requests.post(url, data={"username": "13012345678", "password": "123456", "verify_code": "8888"}, cookies=cookie_data)
print("login response data=", response.json())

# 我的订单：http://localhost/Home/Order/order_list.html
response = requests.get("http://localhost/Home/Order/order_list.html", cookies=cookie_data)
print("order response data=", response.text)