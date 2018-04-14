# -*- coding: UTF-8 -*-
from setting import _db
import MySQLdb

#自动同步数据库表
class _addToDB(_db):

	def __init__(self):
		super(_addToDB,self).__init__()
		self.table_name = ''



	def insert(self):
		pass


	def select(self):
		pass
	