import json
import socket
import telnetlib


class Dubbo(telnetlib.Telnet):
    prompt = 'dubbo>'
    coding = 'utf-8'

    def __init__(self, host=None, port=0,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b"\n")

    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        print("data111==================", data)
        return data

    def invoke(self, service_name, method_name, arg):
        # command_str = "invoke {0}.{1}({2})".format(service_name, method_name, arg)
        command_str = 'invoke {0}.{1}("{2}")'.format(service_name, method_name, arg)

        print("command_str====", command_str)
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        data = data.decode(Dubbo.coding, errors='ignore').split('\n')[0].strip()

        return data




if __name__ == '__main__':
    # count = 10001
    # for num in range(20190919200001, 20190919200006, 2):
    #     count += 100
    conn = Dubbo('211.103.136.244', 6502)  # 这个是dubbo://的IP和端口

    # T_E006_BUDGET_DETAIL
    data1 = {
        "budgetId": "HKYF201908000003",
    }

    result = conn.invoke("UserService", "findByUsername", "admin")
    print("result======", result)
