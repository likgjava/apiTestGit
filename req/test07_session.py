import requests

# 创建session对象
session = requests.Session()

# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
session.get("http://localhost/index.php?m=Home&c=User&a=verify")

# 登录：http://localhost/index.php?m=Home&c=User&a=do_login
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
response = session.post(url, data=data)
print("login response data=", response.json())

# 我的订单：http://localhost/Home/Order/order_list.html
response = session.get("http://localhost/Home/Order/order_list.html")
print("order response data=", response.text)
