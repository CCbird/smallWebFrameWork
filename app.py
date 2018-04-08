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

				if pattern[1] =='js':						#获取js文件路径
					p        = re.search(pattern[0],path)
					js_path  = p.group()
					#print js_path				
					return self.js(js_path)

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

	def img():												#加载img
		pass						

	def js(self,js_path):									#加载js
		status = '200 OK'
		response_headers = [('Content-type','application/javascript')]
		self.start(status,response_headers)
		js_path = os.path.dirname(os.path.realpath(__file__)) + js_path
		f = open(js_path,'r')
		txt = f.read()
		#txt = str(txt)
		yield txt




	def Get_404(self):
		status = '404 Not Found'
		response_headers =[('Content-type','text/plain')]
		self.start(status,response_headers)
		yield "NOT FOUND PAGE!!!!"


