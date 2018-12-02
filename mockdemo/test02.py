import unittest
from unittest import mock


def add(x, y):
    print("该方法还未写完...")
    return 0

def side_effect(*args, **kwargs):
    print("args=", args)
    return 9

class TestAdd2(unittest.TestCase):

    def test_add01(self):
        # mock
        add = mock.Mock(name="mock1", return_value=5, side_effect=side_effect)
        result = add(1, 2)
        print("result111=", result)
        result = add(1, 2)
        print("result222=", result)
        result = add(1, 2)
        print("result333=", result)
        add.side_effect = None
        result = add(1, 2)
        print("result444=", result)



