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

# tokenize模块将在文本之外生成令牌，并且针对每个处理过的行返回一个迭代器
import tokenize
reader = open('amina.py').next
tokens = tokenize.generate_tokens(reader)
print tokens.next() # (1, 'from', (1, 0), (1, 4), 'from amina.quality import similarities\n')
print tokens.next() # (1, 'amina', (1, 5), (1, 10), 'from amina.quality import similarities\n')
print tokens.next()

def power(values):
	for value in values:
		print 'powering %s' % value
		yield value
def adder(values):
	for value in values:
		print 'adding to %s' % value
		if value % 2 == 0:
			yield value + 3
		else:
			yield value + 2
elements = [1, 4, 7, 9, 12, 19]
res = adder(power(elements))
print res.next() # powering 1 adding to 1 3
print res.next() # powering 4 adding to 4 7
print res.next() # powering 7 adding to 7 9

def psychologist():
	print 'Please tell me your problem'
	while True:
		answer = (yield)
		if answer is not None:
			if answer.endswith('?'):
				print ("Don't ask yourself too much questions")
			elif 'good' in answer:
				print "A that's good, go on"
			elif 'bad' in answer:
				print "Don't be so negative"
free = psychologist()
free.next()    # Please tell me you problem
free.send('I feel bad') # Don't be so negative
free.send("why I sholdn't ?") # Don't ask yourself too much questions
free.send("Ok then i should find what is good for me") # A that's good, go on

def my_generator():
	try:
		yield 'something'
	except ValueError:
		yield 'dealing with the exception'
	finally:
		print "ok let's clean"
gen = my_generator()
gen.next()   #'something'
gen.throw(ValueError('mean mean mean')) # 'dealing with the exception'
gen.close() # ok let' clean
gen.next() # Traceback (...)























