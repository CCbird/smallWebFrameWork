# -*- coding: UTF-8 -*-
import MySQLdb
from model import *
from render import *




class blog_list():
	Table   =['post','comment']                #添加的表名

	post    =['ID','Title','Body','Timestamp']      #表属性
	comment =['Content','post','Timestamp']



def admin(context):

	return render('admin/admin.pyhtml',context)
		

'''
context 	= {'Q':{}}

Titles  	= ['一','二','三']
Bodys    	= ['一','二','三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三三12312312311231231231aaasdhdshksdjhsdlkjhdskjsdhkdlsjhdskldshkdjshds']
Timestamps	= ['2018-04-13 22:6:11','2018-04-13 22:6:11','2018-04-13 22:6:11']

for key in List:
	values = eval(key+'s')
	for value in values:
		context['Q'].setdefault(key,[]).append(value)
'''


	





