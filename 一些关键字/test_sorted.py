# -- coding: utf-8 --

x = [11, 23, 21, 13, 14, 10, 24, 55, 54, 29, 44]
y = sorted(x)
print y

# 给sorted设置key作为参数，可以忽略大小写
z = sorted(['bob', 'Boom', 'Zoo', 'about'], key = str,lower)
print z

# 要尽兴反向排序，只需要加reverse
s = sorted(x, reverse = True)
print s
