# -*- coding:utf-8 -*-

import threading
from time import ctime, sleep

def music(func):
	for i in range(2):
		print "I was listening to %s. %s " % (func, ctime())
		sleep(4)

def move(func):
	for i in range(2):
		print "I was at the %s! %s " % (func, ctime())
		sleep(5)

threads = []
t1 = threading.Thread(target = music, args = (u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target = move, args = (u'阿发他',))
threads.append(t2)

if __name__ == '__main__':
	for t in threads:
		t.setDaemon(True) # setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
		t.start() # 开始线程活动。
	t.join() # join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
	print "All over %s" % ctime()