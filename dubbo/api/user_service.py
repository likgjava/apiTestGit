from dubbo.api.base_service import BaseService


class UserService(BaseService):
    service_name = "UserService"
    find_by_username_method = "findByUsername"

    def __init__(self):
        super().__init__()

    def findByUsername(self, username):
        response = self.dubbo_client.invoke(UserService.service_name, UserService.find_by_username_method, username)
        return response
