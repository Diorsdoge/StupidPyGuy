# -- coding: utf-8 --

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print xyz   # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

x = [1, 2, 3]
y = [4, 5, 6, 7]
xy = zip(x, y)
print xy    # [(1, 4), (2, 5), (3, 6)]

x = [1, 2, 3]
x = zip(x)
print x     # [(1,), (2,), (3,)]

x = zip()
print x     # []

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
u = zip(*xyz)
print u    # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

x = [1, 2, 3]
r = zip(* [x] * 3)
print r    # [(1, 1, 1), (2, 2, 2), (3, 3, 3)]

