# -*- coding: utf-8 -*-

def get_allocated(_lst: list):
    return (_lst.__sizeof__() - [].__sizeof__()) // 8


class PyList_Type:
    """一些list类型的操作"""
    tp_name = 'list'

    def append(self, item):
        pass
    # ...


class PyObject:
    _PyObject_HEAD_EXTRA = None
    ob_refcnt = 0
    ob_type = None


class PyVarObject(PyObject):
    ob_size = 0


class PyListObject(PyVarObject):
    ob_type = PyList_Type()
    ob_item = None
    allocated = 0

# l = ["x", "y", "z"]
l = PyListObject()
l.ob_item = ["x", "y", "z"]
l.ob_size = 3
l.allocated = "?"


def list_resize(lst: PyListObject, newsize):
    newsize = lst.ob_size + 1  # 4

    allocated = lst.allocated

    # 不用扩容的情况
    if allocated >= newsize >= allocated/2:
        lst.ob_size = newsize
        return

    # 需要扩容
    # 1. 计算新最大容量
    new_allocated = newsize + (newsize >> 3) + (3 if newsize < 9 else 6)  # 4 + 0 + 3 = 7

    # 2. 分配新内存
    items = [None] * new_allocated

    # 3. 复制到新内存
    # for idx in range(len(lst.ob_item)):
    for idx in range(lst.ob_size):
        items[idx] = lst.ob_item[idx]

    lst.ob_item = items
    lst.ob_size = newsize
    lst.allocated = new_allocated

    return

l.append("q")
# l.ob_item = ["x", "y", "z"]
# l.ob_size = 3
# l.allocated = "?"
l.ob_item = ["x", "y", "z", None, None, None, None]
l.ob_size = 4
l.allocated = 6
l.ob_item = ["x", "y", "z", "q", None, None, None]
