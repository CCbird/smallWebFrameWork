# -*- coding: UTF-8 -*-
import MySQLdb
import datetime
import types
from collections import OrderedDict


              #添加的表名
context 	= {'Q':{}}
context['Q']     = OrderedDict(context['Q'])

list_sort    =['ID','Title','Body','Timestamp']      #表属性
'''
nowtime		=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


IDs         = [1,2,3]
Titles  	= ['一','二','三']
Bodys    	= ['一','二','三三三三skldshkdjshds']
Timestamps	= [nowtime,nowtime,nowtime]

for key in list_sort:
	values = eval(key+'s')
	for value in values:
		context['Q'].setdefault(key,[]).append(value)
'''

def details(*args):
	#print args[0][0]

	ks = []
	for key in list_sort:
		ks.append(key)

	for i in range(len(ks)):	
		buf = args[0][i]
		if type(buf) == datetime.datetime:
			buf = args[0][i].strftime('%Y-%m-%d %H:%M:%S')
		else:
			buf = args[0][i]

			#print type(buf)
		context['Q'].setdefault(ks[i],[]).append(buf)
	print len(context['Q']['ID'])
	


	#print context

# 打开数据库连接
try:
	db = MySQLdb.connect("localhost", "root", "wuwangjie", "blog", charset='utf8' )
except:
	print "连接失败"
# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM post "
arg = []
try:
   # 执行SQL语句
	cursor.execute(sql)
	# 获取所有记录列表
	results = cursor.fetchall()

	for ID in cursor:
		for index in range(len(ID)):
			#print  ID[index]
			arg.append(ID[index])

		#print arg
		details(arg)
		arg = []

				
	
except MySQLdb.Error,e:
	cursor.rollback()
	db.rollback()
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# 关闭数据库连接
db.close()









'''


import collections
context 	= {'Q':{}}
#context['Q'] = collections.OrderedDict()


list_sort   = ['Title','Body','Timestamp']


Titles  	= ['1','2','3']
Bodys    	= ['3','2','1']
Timestamps	= ['2018-04-13 22:6:11','2018-04-13 22:6:11','2018-04-13 22:6:11']

for key in list_sort:
	values = eval(key+'s')
	for value in values:
		context['Q'].setdefault(key,[]).append(value)



for i in range(len(list_sort)):
	for j in range(len(list_sort)):
		print context['Q'][list_sort[j]][i]		

#print context['Q']['Title']
#print sorted(context['Q'],reverse=True)





def context(list_sort,):

	for title in Titles:
		context['Q'].setdefault(Title,[]).append(title)

	for body in Bodys:
		context['Q'].setdefault(Body,[]).append(body)

	for time in Timestamps:
		context['Q'].setdefault(Timestamp,[]).append(time)
'''





'''
d_urls      = [ ('^/index$'                    ,      'index'),
		        ('^/admin$'             	   ,	  'admin'),
		        ('^/admin/add.html$'           ,      'ADD'  ),
		        ('^/admin/post.html$'          , 	  'ADD'  )
		      ]

static_urls = [ ('^/static/css/add.css$' 	   ,  	 'css'  ),
		        ('^/static/css/admin.css$' 	   ,  	 'css'  ),
		        ('^/static/js/getTimeStamp.js$',     'js'   ),
		        ('^/static/js/Submit.js$'      ,     'js'   ),
		        ('^/static/img/1.jpeg$'        ,     'jpeg' )   
		       ]


urls = d_urls + static_urls

print urls





context = {}
titles = 'title'
title = ['one','two','three']
title.append('four')

for t in title:
	context.setdefault(titles,[]).append(t)

#context =  json.dumps(context,encoding="UTF-8",ensure_ascii=False,sort_keys=False, indent=4)

#context = json.loads(context, encoding="UTF-8",ensure_ascii=False)



print context




测试用，无卵用！



from model import blog

class blog_list():
	post   =['Title','body','created','updated']
	comment=['content','created']

#blog_list = blog_list()



def a(app,*args):
	f=getattr(app,args[0][0])
	print f
	print args
	print len(args[0])
	  
					
a(blog,blog_list.post,blog_list.comment)
'''

