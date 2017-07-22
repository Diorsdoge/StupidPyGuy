# -- coding: utf-8 --

# eval()函数只能计算单个表达式的值，而exec()函数可以动态运行代码段。
# eval()函数可以有返回值，而exec()函数返回值永远为None。

x = 10

def func():
    y = 20
    a = eval('x + y')
    print('a: ', a)   # 30
    b = eval('x + y', {'x': 1, 'y': 2})
    print('b: ', b)   # 3
    c = eval('x + y', {'x': 1, 'y': 2}, {'y': 3, 'z': 4})
    print('c: ', c)   # 4
    d = eval('print(x, y)') # 10, 20
    print('d: ', d)	  # None

func()

x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr) # 60
    exec(expr, {'x': 1, 'y': 2}) # 33
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})  # 34
    
func()