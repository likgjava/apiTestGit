import unittest
from unittest import mock


def add(x, y):
    print("该方法还未写完...")
    return 0


class TestAdd(unittest.TestCase):

    def test_add01(self):
        # mock
        add = mock.Mock(name="mock1", return_value=3)
        print("mock add=", add)

        result = add(1, 2)
        print("result=", result)
        self.assertEqual(3, result)
