# -*- coding: utf-8 -*-

"""
@Project : lq_talk 
@File    : 上传图片.py
@Date    : 2023/6/13 10:29:45
@Author  : zhchen
@Desc    : 
"""
import os

import requests

_file_path = "img/20200601155155562.png"

cookies = {
    'cloudreve-session': '',
}


def upload_msg(file_path):
    # 获取文件名
    file_name = os.path.basename(file_path)
    print(file_name)
    file_stat = os.stat(file_path)
    # 最近修改时间
    last_modified = int(file_stat.st_mtime * 1000)
    print(last_modified)
    # 文件大小
    file_size = file_stat.st_size
    print(file_size)
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

    json_data = {
        'path': '/img/',
        'size': file_size,
        'name': file_name,
        'policy_id': 'YGCW',
        'last_modified': last_modified,
    }

    response = requests.put(
        'http://159.75.88.180:5212/api/v3/file/upload',
        cookies=cookies,
        headers=headers,
        json=json_data,
        verify=False,
    )
    print(response)
    print(response.json())
    return response.json()['data']['sessionID']


def upload(file_path, session_id):
    headers = {
        'Content-Type': 'application/octet-stream',
    }
    with open(file_path, 'rb') as f:
        data = f.read()
    url = f'http://159.75.88.180:5212/api/v3/file/upload/{session_id}/0'
    response = requests.post(url, data=data, headers=headers, cookies=cookies, verify=False)
    print(response)
    print(response.json())


if __name__ == '__main__':
    s_id = upload_msg(_file_path)
    upload(_file_path, s_id)
