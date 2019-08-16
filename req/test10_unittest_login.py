# 导包
import unittest
import requests


# 定义测试类
class TestLogin(unittest.TestCase):
    def setUp(self):
        # 创建Session对象
        self.session = requests.Session()

        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self):
        if self.session:
            self.session.close()

    # 定义测试方法
    # 登录成功
    def test_login_success(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        # 断言
        content_type = response.headers.get("Content-Type")
        print("content_type=", content_type)
        self.assertIn("image", content_type)

        # 登录
        login_data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
        response = self.session.post(self.login_url, data=login_data)
        result = response.json()
        print("login response data=", result)
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, result.get("status"))
        self.assertIn("登陆成功", result.get("msg"))

    # 账号不存在
    def test_login_username_is_not_exist(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        # 断言
        content_type = response.headers.get("Content-Type")
        print("content_type=", content_type)
        self.assertIn("image", content_type)

        # 登录
        login_data = {"username": "13088888888", "password": "123456", "verify_code": "8888"}
        response = self.session.post(self.login_url, data=login_data)
        result = response.json()
        print("login response data=", result)
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, result.get("status"))
        self.assertIn("账号不存在", result.get("msg"))

    # 密码错误
    def test_login_pwd_is_error(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        # 断言
        content_type = response.headers.get("Content-Type")
        print("content_type=", content_type)
        self.assertIn("image", content_type)

        # 登录
        login_data = {"username": "13012345678", "password": "error", "verify_code": "8888"}
        response = self.session.post(self.login_url, data=login_data)
        result = response.json()
        print("login response data=", result)
        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, result.get("status"))
        self.assertIn("密码错误", result.get("msg"))
