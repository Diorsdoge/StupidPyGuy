# -- coding: utf-8 --
# 在没完善一个程序之前，我们不知道程序在哪里会出错，与其让它在运行最崩溃，
# 不如在出现错误条件时就崩溃，这时候就需要assert断言的帮助。
# assert 表达式 [, 参数]

a = [1, 2, 3, 4]
len(a)
assert len(a) >= 5, '列表元素个数小于5'