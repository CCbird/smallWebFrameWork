# -*- coding: UTF-8 -*-
from setting import _db
import MySQLdb
from admin import admin
from admin import blog_list
from collections import OrderedDict 





#格式 context 	= {'？？？':{}}





#自动同步数据库表
class DB_L_WEB(_db):

	def __init__(self):
		super(_addToDB,self).__init__()
		self.table_name = ''



	def insert(self):
		pass


	def select(self):
		pass

def migrate(f):
	context 	 = {'Q':{}}
	context['Q'] = OrderedDict(context['Q'])

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

		ks = []
		for key in blog_list.post:
			ks.append(key)


		for ID in cursor:
			for index in range(len(ID)):
				#print ID[0],ID[1],ID[2],ID[3]
				context['Q'].setdefault(ks[index],[]).append(ID[index])

		#print context			
		R=f(context)
				
	except MySQLdb.Error,e:
		cursor.rollback()
		db.rollback()
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

	# 关闭数据库连接
	db.close()
	return R
	