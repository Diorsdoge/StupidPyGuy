# -*- coding:utf-8 -*-

hosts = file('/etc/hosts')
try:
	for line in hosts:
		if line.startsiwth('#'):
			continue
		print line
finally:
	hosts.close()

from __future__ import with_statement
with file('/etc/hosts') as hosts:
	for line in hosts:
		if line.startsiwth('#'):
			continue
		print host

class Context(object):
	def __enter__(self):
		print 'entering the zone'
	def __exit__(self, exception_type, exception_value, exception_traceback):
		print 'leaving the zone'
		if exception_type is None:
			print 'with no error'
		else:
			print 'with an error (%s)' % exception_value

with Context():
	print 'i am the zone'
	






