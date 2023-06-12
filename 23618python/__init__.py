# -*- coding: utf-8 -*-

"""
@Project : lq_talk 
@File    : __init__.py.py
@Date    : 2023/6/5 18:01:40
@Author  : zhchen
@Desc    : 
"""


def bytes_to_01(b: bytes):
    return ''.join([bin(i)[2:].zfill(8) for i in b])


if __name__ == '__main__':
    print('你'.encode('utf-8'))
    print(bytes_to_01('你'.encode('utf-8')))
