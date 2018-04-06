from functools import reduce

__author__ = 'Administrator'

import time

def performance(f):
	def fn(*args,**kwargs):
		t1=time.time()
		r =f(*args,**kwargs)
		t2 = time.time()
		print "call %s() in %fs"%(f.__name__,(t2-t1))
		return r
	return fn

@performance
def factorial(n):
	return reduce(lambda x,y:x*y,range(1,n+1))
print factorial(10)