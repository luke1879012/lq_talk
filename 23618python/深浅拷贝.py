# -*- coding: utf-8 -*-

"""
@Project : lq_talk 
@File    : 深浅拷贝.py
@Date    : 2023/6/14 10:18:56
@Author  : zhchen
@Desc    : 
"""
# https://pythontutor.com/visualize.html#mode=display
from copy import deepcopy

a = {'k1': [2, 3, 4], 'k2': 6}
b = a
c = a.copy()
d = deepcopy(a)

a['k2'] = 7
a['k1'].append(8)
