
#from app import application as request
from model import *


def index():
		context = {
    	'title': 'Tenjin Example',
    	'items': ['<AAA>', 'B&B', '"CCC"'],
		}
		return render('Template/index.pyhtml',context)

