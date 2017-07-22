# -- coding: utf-8 --

# python 异常处理

try:
	"""Do"""
	raise MyError # 自己手动抛出
except Exception as e:
	print "e"
except MyError:
	print "MyError"
else:
	print "pass"
finally:
	print "Over"