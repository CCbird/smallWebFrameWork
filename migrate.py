# -*- coding: UTF-8 -*-
from setting import _db
from admin   import blog_list
import MySQLdb

#自动同步数据库表
class _addToDB(_db):

	def __init__(self):
		super(_addToDB,self).__init__()
		self.table_name = ''


	def create_Table(self,app,*args):
		try:
			db     = MySQLdb.connect(self.host, self.user, self.passwd)
			cursor = db.cursor() 
			cursor.execute('use '+self.db_name)
			print self.db_name
	
		except MySQLdb.Error, e:
			db.rollback()
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])


		try:
			for t in range(len(args)):									#不定参数个数
				self.table_name = blog_list.table[t]					#获取表名
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
			db.rollback()
			print "Mysql Error %d: %s" % (e.args[0], e.args[1])

		db.commit()
		cursor.close()
		db.close()		


	def insert(self,):
		pass


	def select(self):
		pass
	
migration = _addToDB()													#实例化同步类