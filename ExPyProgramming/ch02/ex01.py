# -*- coding: utf-8 -*-

numbers = range(10)
size = len(numbers)
evens = []
i = 0
while i < size:
	if i % 2 == 0:
		evens.append(i)
	i += 1
print evens    # [0, 2, 4, 6, 8]

# 可改为
print [i for i in range(10) if i % 2 == 0]   # [0, 2, 4, 6, 8]



i = 0
seq = ["one", "two", "three"]
for element in seq:
	seq[i] = '%d: %s' % (i, seq[i])
	i += 1
print seq   # ['0': one, '1: two', '2: three']

seq = ["one", "two", "three"]
for i, element in enumerate(seq):
	seq[i] = '%d: %s' % (i, seq[i])
print seq   # ['0': one, '1: two', '2: three']


# 迭代
i = iter('abc')
print i.next()	# 'a'
print i.next()	# 'b'
print i.next()	# 'c'

# 迭代器基于讲个方法：next——返回下一个项目，__iter__——返回迭代器本身
 class MyIterator(object):
 	"""docstring for MyIterator"""
 	def __init__(self, step):
 		self.step = step

 	def next(self):
 		"""Returns the next element."""
 		if self.step == 0:
 			raise StopIteration
 		self.step -= 1
 		return self.step

 	def __iter__(self):
 		"""Returns the iterator itself."""
 		return self

 for e1 in MyIterator(4):
 	print e1 # 3 2 1 0
 		
# 迭代器
def fibonacci():
	a, b = 0, 1
	while True:
		yield b
		a, b = b, a + b
fib = fibonacci()
print fib.next() # 1
print fib.next() # 2
print [fib.next() for i in range(10)] # [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]











