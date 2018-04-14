# -*- coding: UTF-8 -*-

#数据库数据类型

def charField(maxlength):
	s     = 'varchar('+str(maxlength)+')'
	return s

def textField():
	s     = 'text'
	return s

def datetimeField():
	s     = 'datetime'
	return s


def numericalField(Type,Size):
	if Type =='int':
		s     = 'int('+str(Size)+') unsigned NOT NULL'
		return s


	

