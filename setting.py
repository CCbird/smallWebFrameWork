# -*- coding: UTF-8 -*-

import MySQLdb

class _db(object):
	def __init__(self):
		self.host = 'localhost'
		self.port = 3306
		self.user = 'root'
		self.passwd = 'wuwangjie'
		self.db_name = 'ddd'

	
	def create(self):
		try:
			db     = MySQLdb.connect(self.host, self.user, self.passwd)
			cursor = db.cursor()
			cursor.execute('show databases')
			cursor.execute('create database  if not exists '   + self.db_name)					
			db.commit()

		except MySQLdb.Error, e:
				print "Mysql Error %d: %s" % (e.args[0], e.args[1])

		finally:
		# 关闭数据库连接
			db.close()


db = _db()

