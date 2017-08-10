# -*- coding:utf-8 -*-

import itertools

# 窗口迭代器islice
def starting_at_five():
	value = raw_input().strip()
	while value != '':
		for e1 in itertools.islice(value.split(), 4, None):
			yield e1
		value = raw_input().strip()

iter = starting_at_five()
iter.next()
# one two three four five six

# 往返式的迭代器tee
def with_head(iterable, headsize=1):
	a, b = itertools.tee(iterable)
	return list(itertools.islice(a, headsize)), b
with_head(seq)   # ([1], <itertools.tee object at 0x100c698>)
with_head(seq, 4) # ([1, 2, 3, 4], <itertools.tee object at 0x100c670>)

# uniq迭代器 groupby
from itertools import groupby
def compress(data):
	return ((len(list(group)), name) for name, group in groupby(data))

def decompress(data):
	return (car * size for size, car in data)

list(compress('get uuuuuuuuuuuuuuuup'))
compressed = compress('get uuuuuuuuuuuuuuup')
''.join(decompress(compressed))

