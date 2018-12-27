import requests
import unittest


# 获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
# 登录：http://localhost/index.php?m=Home&c=User&a=do_login

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    def test_login_success(self):
        # 获取验证码
        response = self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        print("type=", response.headers.get("Content-Type"))
        self.assertIn("image", response.headers.get("Content-Type"))

        # 登录
        url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
        response = self.session.post(url, data=data)
        print("login response data=", response.json())

        # 断言
        result = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, result.get("status"))
        self.assertEqual("登陆成功", result.get("msg"))

    def test_login_username_is_not_exist(self):
        # 获取验证码
        response = self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        print("type=", response.headers.get("Content-Type"))
        self.assertIn("image", response.headers.get("Content-Type"))

        # 登录
        url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        data = {"username": "13088889999", "password": "123456", "verify_code": "8888"}
        response = self.session.post(url, data=data)
        print("login response data=", response.json())

        # 断言
        result = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, result.get("status"))
        self.assertIn("账号不存在", result.get("msg"))

    def test_login_pwd_is_error(self):
        # 获取验证码
        response = self.session.get("http://localhost/index.php?m=Home&c=User&a=verify")
        print("type=", response.headers.get("Content-Type"))
        self.assertIn("image", response.headers.get("Content-Type"))

        # 登录
        url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        data = {"username": "13012345678", "password": "error", "verify_code": "8888"}
        response = self.session.post(url, data=data)
        print("login response data=", response.json())

        # 断言
        result = response.json()
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, result.get("status"))
        self.assertIn("密码错误", result.get("msg"))
