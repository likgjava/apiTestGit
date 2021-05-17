import json
import unittest

from dubbo.api.member_service import MemberService


class TestMemberService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.member_service = MemberService()

    def test01_find_by_telephone_success(self):
        """查询成功"""
        telephone = "13520196139"
        response = self.member_service.find_by_telephone(telephone)
        print("response===", response)

        json_data = json.loads(response)
        self.assertEqual(telephone, json_data.get("phoneNumber"))

    def test02_find_by_telephone_phone_not_exist(self):
        """手机号不存在"""
        telephone = "13520190001"
        response = self.member_service.find_by_telephone(telephone)
        print("response===", response)

        self.assertEqual("null", response)

    def test03_find_by_telephone_phone_is_empty(self):
        """手机号为空"""
        telephone = ""
        response = self.member_service.find_by_telephone(telephone)
        print("response===", response)

        self.assertEqual("null", response)

    def test04_add_all_fields(self):
        member = {
            "fileNumber": "D001",
            "name": "tom001",
            "sex": "男",
            "idCard": "111111111111",
            "phoneNumber": "13020210002",
            "regTime": "2021-01-01 01:01:00",
            "password": "123",
            "email": "123@qq.com",
            "birthday": "2021-01-01 01:01:00",
            "remark": "备注",
        }
        response = self.member_service.add(member)
        print("response===", response)

        self.assertEqual("null", response)

    def test05_add_all_fields_miss(self):
        member = {}
        response = self.member_service.add(member)
        print("response===", response)

        self.assertEqual("null", response)