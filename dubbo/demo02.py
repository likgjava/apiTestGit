import telnetlib

# 创建telnet连接
telnet = telnetlib.Telnet("211.103.136.244", 6502)

# 调用服务接口
command = 'invoke MemberService.add({"fileNumber":"D0001", "name":"李白", ' \
          '"phoneNumber":"13020210003", "class":"com.itheima.pojo.Member"})'
telnet.write(command.encode())
telnet.write("\n".encode())  # 输入换行符

# 获取响应数据
response = telnet.read_until("dubbo>".encode())
print("response===", response.decode())

# 关闭连接对象
telnet.close()
