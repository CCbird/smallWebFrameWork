# -*- coding: UTF-8 -*-
#from app import application as request
from render import *


def index(context):
	
	return render('Template/index.pyhtml',context)

