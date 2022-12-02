# -*- coding: utf-8 -*-

def get_allocated(_lst: list):
    return (_lst.__sizeof__() - [].__sizeof__()) // 8


# l = ["x", "y", "z", "m", "n"]
# print(f"size = {len(l)} | allocate = {get_allocated(l)}")
# l.append("q")
# print(f"size = {len(l)} | allocate = {get_allocated(l)}")
#
#
# l = list(range(20))
# l.append(1)
# print(f"size = {len(l)} | allocate = {get_allocated(l)}")


print("=" * 100)
l = []
for i in range(20):
    print(f"size = {len(l):2} | allocate = {get_allocated(l):2} | l = {l}")
    l.append(i)
