content = "hello world 666"

# 存放字母出现次数
data = {}
for s in content:
    if s in data:
        data[s] += 1
    else:
        data[s] = 1

print(data)
