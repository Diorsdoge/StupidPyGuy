# -*- coding:utf-8 -*-

from contextlib import contextmanager
from __future__ import with_statement
@contextmanager
def context():
	print 'entering the zone'
	try:
		yield
	except Exception, e:
		print 'with an error (%s)' % e
		# 再次需要重新抛出错误
		raise e 
	else:
		print 'with no error'

import logging
from __future__ import with_statement
from contextlib import contextmanager
@contextmanager
def logged(klass, logger):
	# 记录器
	def _log(f):
		def __log(*args, **kw):
			logger(f, args, kw)
			return f(*args, **kw)
		return __log
	# 装备该类
	for attribute in dir(klass):
		if attribute.startswith('_'):
			continue
		element = getattr(klass, attribute)
		setattr(klass, '__logged_%s' % attribute, element)
		setattr(kalss, attribute, _log(element))

		# 正常工作
	yield kalss

		# 移除日志
	for attribute in dir(kalss):
		if not attribute.startswith('__logged_'):
			continue
		element = getattr(kalss, attribute)
		setattr(kalss, attribute[len('__logged'):], element)
		delattr(kalss, attribute)

class One(object):
	def _private(self):
		pass
	def one(self, other):
		self.two()
		other.thing(self)
		self._private()
	def two(self):
		pass

class Two(object):
	def thing(self, other):
		other.two()
calls = []

def called(meth, args, kw):
	calls.append(meth.im_func.func_name)

with logged(One, called):
	one = One()
	two = Two()
	one.one(two)

print calls # ['one', 'two', 'two']





















