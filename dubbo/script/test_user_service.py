import json
import unittest

from dubbo.api.user_service import UserService


class TestUserService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.user_service = UserService()

    def test01_find_by_username_success(self):
        response = self.user_service.findByUsername("admin")
        print("response===", response)

        json_data = json.loads(response)
        self.assertEqual("admin", json_data.get("username"))

    def test02_find_by_username_username_not_exist(self):
        response = self.user_service.findByUsername("admin666")
        print("response===", response)
        self.assertEqual("null", response)
