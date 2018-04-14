# -*- coding: UTF-8 -*-


from db_datastyle import*


'''
blog程序数据库包含的内容
'''

class blog():
	#文章_表属性
	Title   = charField(maxlength=255)          
	Body	= textField()
	Timestamp = datetimeField()



	#评论_表属性
	Content = textField()
	post    = numericalField(Type='int',Size=11)




