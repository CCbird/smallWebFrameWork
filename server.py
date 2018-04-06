
# -*- coding: UTF-8 -*-
import sys
from wsgiref.simple_server import make_server,demo_app
from app import application as app




if __name__ ==  "__main__":

  if 'runserver' in sys.argv:
	httpd =make_server('',8080,app)
	sa =httpd.socket.getsockname()
	print 'http://{0}:{1}/'.format(*sa)
	httpd.serve_forever()
  elif 'createdatabase' in sys.argv:
  		from  setting import db
		db.create()
  else:
	print "Less args!!!\n"

