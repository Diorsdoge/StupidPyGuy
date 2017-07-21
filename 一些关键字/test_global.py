# -- coding: utf-8 --
# 定义为全局变量

def function():
	global xticks
	
	print "x is ", x
	x = 2
	print 'Changed local x to', x

x = 50
function()
print 'Value of x is', x