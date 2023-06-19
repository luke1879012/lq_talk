# -*- coding: utf-8 -*-

"""
@Project : lq_talk 
@File    : 重试.py
@Date    : 2023/6/19 11:19:40
@Author  : zhchen
@Desc    : 
"""
import time


class ShovelError(Exception):
    msg = 'shovel 挂了'
    def alert(self):
        print(f"报警: {self.msg}")

class SlideError(ShovelError):
    msg = '遇到滑块了'
    pass


class RequestsError(ShovelError):
    msg = '请求出错了'
    pass


def retry(func):
    times = 3

    def inner():
        for i in range(times):
            try:
                return func()
            except Exception as e:
                if i != times - 1:
                    print(f"第{i + 1}次重试，错误信息{e}")
                time.sleep(1)
        else:
            raise RequestsError("重试次数用完了")

    return inner


@retry
def requests():
    print("请求")
    raise ConnectionError("连接超时")
    return "data"


try:
    print(requests())
except RequestsError as e:
    e.alert()
except ShovelError as e:
    e.alert()
except Exception:
    print("出现其他未处理异常")
