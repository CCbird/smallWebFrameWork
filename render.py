import tenjin
#tenjin.set_template_encoding('utf-8')  # optional (defualt 'utf-8')
from tenjin.helpers import *
from tenjin.html import *
#import tenjin.gae; tenjin.gae.init()   # for Google App Engine




def render(html,context):
	engine = tenjin.Engine()
	renderF = engine.render(html, context)
	return renderF