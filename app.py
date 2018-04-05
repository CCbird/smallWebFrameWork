import re
from url import urls

class application:
	

	def __init__(self,environ,start_response):
		self.environ = environ
		self.start   = start_response

	def __iter__(self):
		path = self.environ['PATH_INFO']
		for pattern in urls:
			m = re.match(pattern[0],path)
			if m:
				function = getattr(self,pattern[1])
				print pattern[1]
				return function()
		return self.Get_404()		

	def index(self):
		status = '200 OK'
		response_headers = [('Content-type','text/plain')]
		self.start(status,response_headers)
		yield "Welcome!!"

	def hello(self):
		status = '200 OK'
		response_headers = [('Content-type','text/plain')]
		self.start(status,response_headers)
		yield "HELLO!!"

	def Get_404(self):
		status = '404 Not Found'
		response_headers =[('Content-type','text/plain')]
		self.start(status,response_headers)
		yield "NOT FOUND PAGE!!!!"

	def post(self):
		status = '200 OK'
		response_headers = [('Content-type','text/plain')]
		self.start(status,response_headers)

