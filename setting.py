# -*- coding: UTF-8 -*-

import MySQLdb

class _db(object):
	def __init__(self):
		self.host = 'localhost'
		self.port = 3306
		self.user = 'root'
		self.passwd = 'wuwangjie'
		self.db_name = 'blog'

	
	def create(self):
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


db = _db()

