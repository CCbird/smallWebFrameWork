# -*- coding: UTF-8 -*-
from render import *
from model import *


class blog_list():
	table   =['post','comment']                        #添加的表名

	post    =['Title','body','created','updated']      #表属性
	comment =['content','created']



def admin():
	context = {'title':'第一篇博客'}
	return render('Template/admin.pyhtml',context)





