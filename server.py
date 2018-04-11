# -*- coding: UTF-8 -*-
import sys
from wsgiref.simple_server import make_server,demo_app
from app import application as app
from admin import blog_list
from model import blog



if __name__ ==  "__main__":

  if 'runserver' in sys.argv:                #启动服务器
    	httpd =make_server('',8080,app)
    	sa =httpd.socket.getsockname()
    	print 'http://{0}:{1}/'.format(*sa)
    	httpd.serve_forever()
  elif 'createdatabase' in sys.argv:         #创建数据库
      from  setting import db
      db.create()
  elif 'migrate' in sys.argv:                #同步数据库
      from migrate import migration
      migration.create_Table(blog,blog_list.post,blog_list.comment)

  else:
	print "Less args!!!\n"

