# -*- coding: utf-8 -*-

# 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
# enumerate多用于在for循环中得到计数

list = ["这", "是", "一个", "测试"]
for index, item in enumerate(list):
	print index, item

# enumerate还可以接收第二个参数，用于指定索引起始值
list = ["这", "是", "一个", "测试"]
for index, item in enumerate(list, 1):
	print index, item

# 补充：如果要统计文件的行数，可以这样写
count = -1
for index, line in enumerate(open("text.txt"), 'r'):
	count += 1