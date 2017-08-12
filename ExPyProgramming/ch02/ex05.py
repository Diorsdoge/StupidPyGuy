# -*- coding:utf-8 -*-

class WhatFor(object):
	def it(cls):
		print 'work with %s' % cls

	it = classmethod(it)

	def uncommon():
		print 'I could be a global function'
	uncommon = staticmethod(uncommon)

# 装饰器
class WhatFor(object):
	@classmethod
	def it(cls):
		print 'work with %s' % cls

	@staticmethod
	def uncommon():
		print 'I could be a global function'

def mydecorator(function):
	def _mydecorator(*args, **kw):
		# 在调用实际函数之前做些填充工作
		res = function(*args, **kw)
		# 昨晚某些填充工作之后
		return res
	# 返回子函数
	return _mydecorator

def mydecorator(arg1, arg2):
	def _mydecorator(function):
		def __mydecorator(*args, **kw):
			# 在调用实际函数之前做些填充工作
			res = function(*args, **kw)
			# 昨晚某些填充工作之后
			return res
		# 返回子函数
		return __mydecorator
	return _mydecorator

from itertools import izip
rpc_info = {}
def xmlrpc(in_=(), out=(type(None),)):
	def _xmlrpc(function):
		# 注册签名
		func_name = function.func_name
		rpc_info[func_name] = (in_, out)

		def _check_types(elements, types):
			"""Subfunction that checks the types."""
			if len(elements) != len(types):
				raise TypeError('argument count is wrong')
			typed = enumerate(izip(elements, types))
			for index couple in typed:
				arg, of_the_right_type = couple
				if isinstance(arg, of_the_right_type):
					continue
				raise TypeError('arg #%d should be %s') % (index, of_the_right_type)

		# 封装函数
	def __xmlrpc(*args):	# 没有允许的关键字
		# 检测输入的内容
		checkable_args = args[1:] # removing self
		_check_types(checkable_args, in_)
		# 执行该函数
		res = function(*args)

		# 检查输出的内容
		if not type(res) in (tuple, list):
			checkable_res = (res, )
		else:
			checkable_res = res
		_check_types(checkable_res, out)

		# 函数及其类型检查成功
		return res
	return __xmlrpc
return _xmlrpc
		

class RPCView(object):
	@xmlrpc((int, int)) # two int -> None
	def meth1(self, int1, int2):
		print 'received %d and %d' % (int1, int2)

	@xmlrpc((str), (int,)) # string -> int
	def meth2(self, phrase):
		print 'received %s' % phrase
		return 12












