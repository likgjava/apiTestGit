import json
import telnetlib


telnet = telnetlib.Telnet("211.103.136.244", 6502)
# telnet.write(b'\n')

# s = telnet.read_until('dubbo>'.encode())
# telnet.write(b'invoke UserService.findByUsername("admin")\n')
telnet.write('invoke UserService.findByUsername("admin")\n'.encode())
# print("ssssssss111====", s)

s2 = telnet.read_until('dubbo>'.encode())
# telnet.write(''.encode() + b'\n')
print("ssssssss222====", s2)
print("ssssssss222====", s2.decode())


# 添加会员
# command = 'invoke MemberService.add({"id":62,"fileNumber":"d002", "name":"tom2", "class":"com.itheima.pojo.Member"})'
# telnet.write(command.encode() + b"\n")
#
# s3 = telnet.read_until('dubbo>'.encode())
# print("s3====", s3.decode())

# CheckItemService
# command = 'invoke CheckItemService.add({"code":"c002", "name":"体重体检", "class":"com.itheima.pojo.CheckItem"})'
# telnet.write(command.encode() + b"\n")
#
# s3 = telnet.read_until('dubbo>'.encode())
# print("s3====", s3.decode())

# OrderSettingService
# order_setting_list = [
#     {"orderDate":"2021-05-14 01:00:00", "number":100},
#     {"orderDate":"2021-05-15 01:00:00", "number":200, "class":"com.itheima.pojo.OrderSetting"},
# ]
# command = 'invoke OrderSettingService.add({})'.format(json.dumps(order_setting_list))
# print("command===", command)
# telnet.write(command.encode() + b"\n")
#
# s3 = telnet.read_until('dubbo>'.encode())
# print("s3====", s3.decode())


# CheckGroupService
CheckGroup = {"code":"g001", "name":"色盲36项", "class":"com.itheima.pojo.CheckGroup"}
command = 'invoke CheckGroupService.add([97, 98], {})'.format(json.dumps(CheckGroup))
print("command===", command)
telnet.write(command.encode() + b"\n")

s3 = telnet.read_until('dubbo>'.encode())
print("s3====", s3.decode())



print("1111111111")
telnet.close()
print("222222222")



