import requests

# requests.get("http://www.baidu.com", params="kw=python")
requests.get("http://www.baidu.com", params={"kw": "python", "aihao": ["yy", "cg"]})
