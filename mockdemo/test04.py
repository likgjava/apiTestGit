import unittest
from unittest import mock
from mockdemo.sample import OrderPayService, UserService


class TestGenOrder(unittest.TestCase):

    def test01(self):
        """测试余额不足"""

        # mock 获取用户金额接口的返回值为1000
        UserService.get_user_amount = mock.Mock(return_value=1000)

        # 调用下单接口，查看返回结果
        order_pay_service = OrderPayService()
        result = order_pay_service.order_pay()
        print("result=", result)

        # 断言
        self.assertEqual(-1, result.get('status'))
        self.assertEqual('支付失败', result.get('msg'))

    def test02(self):
        """用户不存在"""
        user_service = UserService()
        user_service.get_user_amount = mock.Mock(
            return_value=0, side_effect=Exception("Mock用户不存在的异常")
        )

        # 异常断言
        self.assertRaises(Exception, user_service.get_user_amount, (-1,))


    # 1 利用patch来实现
    @mock.patch("mockdemo.sample.UserService")
    def test03(self, mock_UserInfo):
        # 生成userinfo的实例
        userinfo = mock_UserInfo.return_value
        # mock调用获取用户金额接口的返回值，值为3000
        userinfo.get_user_amount.return_value = 3000
        # 调用下单接口进行支付，查看返回结果
        genOrder = OrderPayService()
        result = genOrder.gen_order()
        # 查看结果
        print(result)
        self.assertEqual(1, result.get('status'))
        self.assertEqual('支付成功', result.get('msg'))
