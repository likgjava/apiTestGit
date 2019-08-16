import unittest
from unittest import mock


# 实现加法操作
def add(x, y):
    print("该方法还未完成...")
    return 0


class TestAdd(unittest.TestCase):

    def test_add(self):
        # 模拟一个mock对象，代替真实的对象，并设置对象的行为
        # mock_obj = mock.Mock(name="mock1", return_value=3)
        # 使用mock对象体换真实的对象
        # add = mock_obj

        add = mock.Mock(name="mock1", return_value=3)

        result = add(1, 2)
        print("result=", result)

        # 断言
        self.assertEqual(3, result)
