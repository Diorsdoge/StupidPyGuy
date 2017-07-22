# -- coding: utf-8 --

# 带有 yield 的函数在 Python 中被称之为 generator（生成器)

# yield 的好处是显而易见的，把一个函数改写为一个 generator 
# 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值
# f = fab(5)
# f.next()
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1


# 利用固定长度的缓冲区来不断读取文件内容。通过 yield，我们不再需要
# 编写读文件的迭代类，就可以轻松实现文件读取：
def read_file(fpath): 
	BLOCK_SIZE = 1024 
	with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
            	yield block 
           	else: 
                return