# -*- coding: utf-8 -*-

"""
@Project : lq_talk 
@File    : 装饰器.py
@Date    : 2023/6/19 11:17:24
@Author  : zhchen
@Desc    : 
"""


def pt():
    print("hello")


def df(func):
    def inner():
        func()
        print("world")

    return inner


pt = df(pt)
pt()