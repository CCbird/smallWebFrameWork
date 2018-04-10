# -*- coding: UTF-8 -*-
import re
import views
import render
from url import urls
import admin
import os,sys



class application:
	

	def __init__(self,environ,start_response):
		self.environ = environ
		self.start   = start_response

	def __iter__(self):
		path = self.environ['PATH_INFO']

		for pattern in urls:
			m = re.match(pattern[0],path)

			if m:
				if pattern[1] =='admin':
					function = getattr(admin,pattern[1])
					return self.admin(function)


				if pattern[1] =='js' or pattern[1] =='css' or  pattern[1] =='jpeg' or pattern[1] =='png':						#获取js文件路径
					#print "到静态了\n"	
					p          = re.search(pattern[0],path)
					resources  = p.group()	
					return self.static(resources_path=resources,style=pattern[1])

				function = getattr(views,pattern[1])
				return self.view(function)				
		return self.Get_404()	

	def view(self,func):									#主页
		status = '200 OK'
		response_headers = [('Content-type','text/html')]
		self.start(status,response_headers)
		yield func()

	def admin(self,func):									#后台界面
		status = '200 OK'
		response_headers = [('Content-type','text/html')]
		self.start(status,response_headers)
		yield func()

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