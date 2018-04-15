# -*- coding: UTF-8 -*-
from admin   import blog_list
import MySQLdb

class _db(object):
	def __init__(self):
		self.host = 'localhost'
		self.port = 3306
		self.user = 'root'
		self.passwd = 'wuwangjie'
		self.db_name = 'blog'
		self.table_name = ''

	
	def create_db(self):
		try:
			db     = MySQLdb.connect(self.host, self.user, self.passwd)
			cursor = db.cursor()
			cursor.execute('show databases')
			cursor.execute('CREATE DATABASE  '+ self.db_name +' DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')					
			db.commit()

		except MySQLdb.Error, e:
				db.rollback()
				print "Mysql Error %d: %s" % (e.args[0], e.args[1])

		finally:
		# 关闭数据库连接
			db.close()

	def create_Table(self,app,*args):

		try:
			try:
				db     = MySQLdb.connect(self.host, self.user, self.passwd)
				cursor = db.cursor() 
				cursor.execute('use '+self.db_name)
				print self.db_name
		
			except MySQLdb.Error, e:
				cursor.rollback()
				db.rollback()
				print "Mysql Error %d: %s" % (e.args[0], e.args[1])


			try:
				for t in range(len(args)):                                 #不定参数个数
					self.table_name = blog_list.Table[t]				   #获取表名
					sql_table="""
							  CREATE TABLE `""" + self.table_name + """` 
							  (
							  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
							   PRIMARY KEY (`id`)
							  ) ENGINE=InnoDB DEFAULT CHARSET=utf8
						  """
					cursor.execute(sql_table)
					for t_value in range(len(args[t])):						#args[t]为不定参数名
						#print len(args[0])
						vals=getattr(app,args[t][t_value])					#获取表属性数据类型
						sql_add="alter table "+self.table_name+" add column "+args[t][t_value]+" "+vals+" NOT NULL"  #为表增加一列
						cursor.execute(sql_add)
			except MySQLdb.Error, e:
				cursor.rollback()
				db.rollback()
				print "Mysql Error %d: %s" % (e.args[0], e.args[1])
		except MySQLdb.Error,e:
			cursor.rollback()
			db.rollback()
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])

		db.commit()
		cursor.close()
		db.close()	


db = _db()

