# -*- coding: UTF-8 -*-
import os

f = open('/Users/jay/Documents/webframework/admin/add.html','r')
txt = f.read()
print txt




'''
测试用，无卵用！



from model import blog

class blog_list():
	post   =['Title','body','created','updated']
	comment=['content','created']

#blog_list = blog_list()



def a(app,*args):
	f=getattr(app,args[0][0])
	print f
	print args
	print len(args[0])
	  
					
a(blog,blog_list.post,blog_list.comment)
'''

