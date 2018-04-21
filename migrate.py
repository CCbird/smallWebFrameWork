# -*- coding: UTF-8 -*-
from setting import _db
import MySQLdb
from admin import admin
from admin import blog_list
from collections import OrderedDict 
import datetime





#格式 context 	= {'？？？':{}}





#自动同步数据库表
class DB_L_WEB(_db):

	def __init__(self):
		super(DB_L_WEB,self).__init__()
		self.table_name = ''



	def insert(self,Title,Body,Timestamp):
		try:
			db     = MySQLdb.connect(self.host, self.user, self.passwd, self.db_name, charset='utf8' )
			print self.host, self.user, self.passwd, self.db_name
		except:
			print '连接失败'
		cursor = db.cursor()
		
		Title = Title[0]
		Body  = Body[0]
		Timestamp = Timestamp[0]
		
		print Title,Body
		print Timestamp

		#sql= "insert into post (Title,Body,Timestamp) VALUES ("+title+','+Body+','+Timestamp+')'
		#for table in blog_list.Table:
			#for key in blog_list.table:
		
		try:	
			cursor.execute("INSERT INTO post (Title,Body,Timestamp) VALUES "+"("+"'"+Title+"'"+','+"'"+Body+"'"+','+'"'+Timestamp+'"'+")")
			#cursor.execute("insert into post (Title,Body,Timestamp) values "+"("+Title+","+Body+","+Timestamp+")")
			print  '增加一条数据'
		except MySQLdb.Error,e:
			#cursor.rollback()
			#db.rollback()
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])	

		#cursor.close()
		db.commit()                   #注意要提交命令！！
		db.close()

	def delete(self,ID):
		try:
			db     = MySQLdb.connect(self.host, self.user, self.passwd, self.db_name, charset='utf8' )
			print self.host, self.user, self.passwd, self.db_name
		except:
			print '连接失败'
		cursor = db.cursor()

		ID = ID[0]
		
		print "Table_ID:"+ID


		#sql= "insert into post (Title,Body,Timestamp) VALUES ("+title+','+Body+','+Timestamp+')'
		#for table in blog_list.Table:
			#for key in blog_list.table:
		
		try:	
			cursor.execute("delete from post where id="+ID)
			#cursor.execute("insert into post (Title,Body,Timestamp) values "+"("+Title+","+Body+","+Timestamp+")")
			print  '删除一条数据'
		except MySQLdb.Error,e:
			#cursor.rollback()
			#db.rollback()
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])	

		#cursor.close()
		db.commit()                   #注意要提交命令！！
		db.close()
		

def migrate(f):
	context 	 = {'Q':{}}
	context['Q'] = OrderedDict(context['Q'])

	try:
		db = MySQLdb.connect("localhost", "root", "wuwangjie", "blog", charset='utf8' )
		#db = MySQLdb.connect(self.host, self.user, self.passwd, self.db_name, charset='utf8' )
	except:
		print "连接失败"
	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	# SQL 查询语句

	sql = "SELECT * FROM post "
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
				#print type(ID[3])
				buf=ID[index]
				if type(buf) == datetime.datetime:
					buf = buf.strftime('%Y-%m-%d %H:%M:%S')
				context['Q'].setdefault(ks[index],[]).append(buf)

		#print context			
		R=f(context)
				
	except MySQLdb.Error,e:
		cursor.rollback()
		db.rollback()
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])

	# 关闭数据库连接
	db.close()
	return R


DB_OP = DB_L_WEB()

	