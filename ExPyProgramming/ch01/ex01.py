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

