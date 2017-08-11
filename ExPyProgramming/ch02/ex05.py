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
