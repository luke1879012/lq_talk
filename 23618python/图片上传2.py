import json
import os
import time

import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'http://159.75.88.180:5212',
    'Pragma': 'no-cache',
    'Referer': 'http://159.75.88.180:5212/home?path=%2F',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
file_path = 'img/20200601155155562 - 副本.png'
# 获取文件状态信息
file_stat = os.stat(file_path)

last_modified_time = int(file_stat.st_mtime * 1000)
print(f"{last_modified_time=}")

name = os.path.basename(file_path)
print(f"{name=}")

size = file_stat.st_size
print(f"{size=}")
data = {
    "last_modified": last_modified_time,
    "name": name,
    "path": "/",
    "policy_id": "YGCW",
    "size": size,
}
print(f'{data=}')
cookies = {
    "cloudreve-session": ""
}
response = requests.put('http://159.75.88.180:5212/api/v3/file/upload',
                        headers=headers, json=data, cookies=cookies)
print(response)
print(response.text)
s_id = response.json()['data']['sessionID']
print(s_id)
h2 = {
    'Content-Type': 'application/octet-stream'
}
with open(file_path, "rb") as f:
    data = f.read()
res2 = requests.post(f'http://159.75.88.180:5212/api/v3/file/upload/{s_id}/0',
                     data=data, headers=h2, cookies=cookies)
print(res2)