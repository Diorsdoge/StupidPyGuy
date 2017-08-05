# -*- coding:utf-8 -*-

# filter(function, iterable)：过滤器，返回由使函数 function 返回True的 iterable 元素组成的迭代器。
lst = [1, 2, 3, 4, 5, 6, 7, 8]
f = lambda x: x%2 == 0
print list(filter(f, lst))