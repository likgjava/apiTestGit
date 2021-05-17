from dubbo.api.base_service import BaseService


class MemberService(BaseService):
    """会员服务接口"""

    def __init__(self):
        super().__init__()
        self.service_name = "MemberService"
        self.find_by_telephone_method = "findByTelephone"
        self.add_method = "add"
        self.find_member_count_by_months_method = "findMemberCountByMonths"

    def find_by_telephone(self, telephone):
        return self.dubbo_client.invoke(self.service_name, self.find_by_telephone_method, telephone)

    def add(self, member):
        member["class"] = "com.itheima.pojo.Member"
        return self.dubbo_client.invoke(self.service_name, self.add_method, member)

    def find_member_count_by_months(self, months):
        return self.dubbo_client.invoke(self.service_name, self.find_member_count_by_months_method, months)
