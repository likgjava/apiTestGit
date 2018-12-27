import requests

response = requests.get("http://www.baidu.com", headers={"area": "010", "name": "tom"})
