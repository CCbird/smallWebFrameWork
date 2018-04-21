# -*- coding: UTF-8 -*-
import re
import views
from url import urls
import migrate
import os,sys
from cgi import parse_qs
import admin
import json
from migrate import DB_OP


class application:
	

	def __init__(self,environ,start_response):
		self.environ = environ
		self.start   = start_response

	def __iter__(self):
		path = self.environ['PATH_INFO']


		try:
			request_body_size = int(self.environ.get('CONTENT_LENGTH',0))
			request_body = self.environ['wsgi.input'].read(request_body_size)
			d = parse_qs(request_body)

			if d.get('Timestamp')!=None:
				print "request_body_size:"+str(request_body_size)
				title     = d.get('Title')
				body      = d.get('contentText')
				timestamp = d.get('Timestamp')
				#title 	  = json.dumps(title, encoding="UTF-8", ensure_ascii=False)
				#body  	  = json.dumps(body, encoding="UTF-8", ensure_ascii=False)
				#timestamp = json.dumps(timestamp, encoding="UTF-8", ensure_ascii=False)

				#print str(title),body,timestamp
				DB_OP.insert(title,body,Timestamp=timestamp)
				#try:
				#	DB_OP.insert(title,body,timestamp)
				#except:
				#	print '失败'


			if d.get('ID')!=None:
				print "request_body_size:"+str(request_body_size)
				ID = d.get('ID')

				DB_OP.delete(ID)

				
				 
		except(ValueError):
			request_body_size = 0

		
		for pattern in urls:
			m = re.match(pattern[0],path)

			if m:

				if pattern[1] =='admin':
					function = getattr(migrate,'migrate')	
					return self.admin(function)

				if pattern[1] =='ADD' or pattern[1]=='CHANGE':	
					p          = re.search(pattern[0],path)
					path  = p.group()
					return self.admin_ACTION(admin=path,action=pattern[1])


				if pattern[1] =='js' or pattern[1] =='css' or  pattern[1] =='jpeg' or pattern[1] =='png':						#获取js文件路径
					#print "到静态了\n"	
					p          = re.search(pattern[0],path)
					resources  = p.group()	
					return self.static(resources_path=resources,style=pattern[1])

				function = getattr(migrate,'migrate')
				return self.view(function)				
		return self.Get_404()	

	def view(self,func):									#主页
		status = '200 OK'
		response_headers = [('Content-type','text/html')]
		self.start(status,response_headers)
		f = getattr(views,'index')
		yield func(f)

	def admin(self,func):									#后台界面
		status = '200 OK'
		response_headers = [('Content-type','text/html')]
		self.start(status,response_headers)
		f = getattr(admin,'admin')
		yield func(f)

	def admin_ACTION(self,admin,action):									#后台界面
		status = '200 OK'
		if   action=='ADD'  :
			response_headers = [('Content-type','text/html')]
		elif action=='CHANGE' : 
			response_headers = [('Content-type','text/html')] 
		else:
			pass
		self.start(status,response_headers)
		admin = os.path.dirname(os.path.realpath(__file__)) + admin
		print admin
		f = open(admin,'r')
		txt = f.read()
		yield txt

	def static(self,resources_path,style):									#加载静态资源
		status = '200 OK'
		
		if   style=='js'  :
			response_headers = [('Content-type','application/javascript')]
		elif style=='css' : 
			response_headers = [('Content-type','text/css')] 
		elif style=='jpeg':
			response_headers = [('Content-type','image/jpeg')]
		elif style=='png' :
			response_headers = [('Content-type','image/png')]
		else:
			pass
		
		self.start(status,response_headers)
		resources_path = os.path.dirname(os.path.realpath(__file__)) + resources_path
		f = open(resources_path,'r')
		txt = f.read()
		yield txt




	def Get_404(self):
		status = '404 Not Found'
		response_headers =[('Content-type','text/plain')]
		self.start(status,response_headers)
		yield "NOT FOUND PAGE!!!!"