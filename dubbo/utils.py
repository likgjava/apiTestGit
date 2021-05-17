import json
import telnetlib


class DubboClient:

    def __init__(self, host, port):
        self.telnet = telnetlib.Telnet(host, port)

    def invoke(self, service_name, method_name, *args):
        """
        调用接口
        :param service_name: 服务名称
        :param method_name: 方法名称
        :param args: 方法参数列表
        :return: 接口响应数据
        """
        # 处理参数
        new_args = self._deal_args(args)
        print("new_args==", new_args)

        # 调用接口
        command = "invoke {}.{}({})\n".format(service_name, method_name, new_args)
        print("command==", command)
        self.telnet.write(command.encode())

        # 读取响应数据
        response_data = self.telnet.read_until("dubbo>".encode())
        print("response_data==", response_data)

        # 处理响应数据
        data = self._deal_response_data(response_data)
        return data

    def _deal_response_data(self, response_data):
        """处理响应数据"""
        data = response_data.decode().split()[0]
        return data

    def _deal_args(self, args):
        """处理参数"""
        args_str = ""
        for arg in args:
            args_str += json.dumps(arg) + ","
        return args_str[:-1]

    def close(self):
        """关闭连接对象"""
        if self.telnet:
            self.telnet.close()
            self.telnet = None

    def __del__(self):
        self.close()


if __name__ == '__main__':
    dubbo_client = DubboClient("211.103.136.244", 6502)

    # result = dubbo_client.invoke("UserService", "findByUsername", "admin")
    # print("result1111111=======", result)
    #
    # result = dubbo_client.invoke("MemberService", "add", {"id":62,"fileNumber":"d002", "name":"tom2", "class":"com.itheima.pojo.Member"})
    # print("result222=======", result)
    #
    # order_setting_list = [
    #     {"orderDate":"2021-05-14 01:00:00", "number":100},
    #     {"orderDate":"2021-05-15 01:00:00", "number":200, "class":"com.itheima.pojo.OrderSetting"},
    # ]
    # result = dubbo_client.invoke("OrderSettingService", "add", order_setting_list)
    # print("result333=======", result)
    #
    # CheckGroup = {"code": "g001", "name": "色盲36项", "class": "com.itheima.pojo.CheckGroup"}
    # result = dubbo_client.invoke("CheckGroupService", "add", [97, 98], CheckGroup)
    # print("result444=======", result)

    result = dubbo_client.invoke("CheckItemService", "findAll")
    print("result555=======", result)
