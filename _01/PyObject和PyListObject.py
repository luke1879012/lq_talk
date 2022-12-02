# -*- coding: utf-8 -*-

class PyObject:
    _PyObject_HEAD_EXTRA = None  # debug
    ob_refcnt = 0
    ob_type = None


class PyVarObject(PyObject):
    ob_size = 0  # len


class PyListObject(PyVarObject):
    # ob_type = None
    ob_item = None
    allocated = 0  # 最大容量


# l = ["x", "y", "z", "m", "n"]
l = PyListObject()
l.ob_item = ["x", "y", "z", "m", "n"]
l.ob_size = 5  # len
l.allocated = 5


def list_resize(lst: PyListObject, newsize):
    newsize = lst.ob_size + 1  # 5 + 1 = 6
    allocated = lst.allocated

    # 不需要扩容
    if allocated >= newsize >= allocated / 2:
        lst.ob_size = newsize
        return

    # 需要扩容的情况
    # 1. 扩容计算公式
    new_allocated = newsize + (newsize >> 3) +\
                   (3 if newsize < 9 else 6)

    # 2. 计算需要内存空间
    new_items = [None] * new_allocated

    # 3. 复制到新数组
    for idx in range(lst.ob_size):
        new_items[idx] = lst.ob_item[idx]

    lst.ob_item = new_items
    lst.ob_size = newsize
    lst.allocated = new_allocated
    return

l.append("q")
