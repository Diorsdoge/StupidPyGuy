# -*- coding:utf-8 -*-

# 应该尽量避免多进程共享资源。多进程共享资源必然会带来进程间相互竞争。而这种竞争又会造成race condition，我们的结果有可能被竞争的不确定性所影响。但如果需要，我们依然可以通过共享内存和Manager对象这么做。


import os
import threading
import multiprocessing
count_thread = 0
count_process = 0

# worker function
def worker1(sign, lock):
	global count_thread
	lock.acquire()
	count_thread += 1
	print (sign, os.getpid())
	lock.release()

def worker2(sign, lock):
	global count_process
	lock.acquire()
	count_process += 1
	print(sign, os.getpid())
	lock.release()

print ('main:', os.getpid())

# Multi-thread
record = []
lock = threading.Lock()
for i in range(5):
	thread = threading.Thread(target=worker1, args=('thread', lock))
	thread.start()
	record.append(thread)

for thread in record:
	thread.join()

# Muti-Process
record = []
lock = multiprocessing.Lock()
for i in range(5):
	process = multiprocessing.Process(target=worker2, args=('process', lock))
	process.start()
	record.append(process)
for process in record:
	process.join()

print count_thread
print count_process

# 共享内存
def f(n, a):
	n.value = 3.14
	a[0] = 5
num = multiprocessing.Value('d', 0.0)
arr = multiprocessing.Array('i', range(10))

p = multiprocessing.Process(target=f, args=(num, arr))
p.start()
p.join()

print num.value
print arr[:]

# Manager

def f(x, arr, l):
	x.value = 3.14
	arr[0] = 5
	l.append('Hello')

server = multiprocessing.Manager()
x = server.Value('d', 0.0)
arr = server.Array('i', range(10))
l = server.list()

proc = multiprocessing.Process(target=f, args=(x, arr, l))
proc.start()
proc.join()

print (x.value)
print (arr)
print (l)









