# 请求TPshop项目的登录接口，请求数据（username: 13088888888, password: 123456, verify_code: 1234）
# 登录接口URL：http://localhost/index.php?m=Home&c=User&a=do_login


# 1.导包
import requests

# 2.发送POST请求
url = "http://localhost/index.php?m=Home&c=User&a=do_login"
data = {
    "username": "13088888888",
    "password": "123456",
    "verify_code": "1234",
}
response = requests.post(url, data=data)

# 3.获取响应数据
print("text=", response.text)
print("text=", response.json())
