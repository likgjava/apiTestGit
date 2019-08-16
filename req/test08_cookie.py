# 使用requests库调用TPshop登录功能的相关接口，完成登录操作
# 登录成功后获取‘我的订单’页面的数据

# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login
# 我的订单：http://localhost/Home/Order/order_list.html


# 1.导包
import requests

# 2.发送请求
# 获取验证码
response = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
cookies = response.cookies
print("cookies=", cookies)
PHPSESSID = cookies.get("PHPSESSID")
print("PHPSESSID=", PHPSESSID)

# 登录
# username=13012345678&password=123456&verify_code=8888
data = {
    "username": "13012345678",
    "password": "123456",
    "verify_code": "8888",
}
cookie_data = {
    "PHPSESSID": PHPSESSID
}
response = requests.post("http://localhost/index.php?m=Home&c=User&a=do_login", data=data, cookies=cookie_data)
print("json data=", response.json())

# 我的订单
response = requests.get("http://localhost/Home/Order/order_list.html", cookies=cookie_data)
print("text=", response.text)

# 3.获取响应数据






