# -*- coding: UTF-8 -*-
#from app import application as request
from render import *


def index():
	context = {'title': '窝窝 \'s Blog'}
	
	return render('Template/index.pyhtml',context)

