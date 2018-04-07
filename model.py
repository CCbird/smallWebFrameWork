from db_datastyle import*

#blog程序数据库包含的内容


class blog():
	#文章_表属性
	Title   = charField(maxlength=255)          
	body	= textField()
	created = datetimeField()
	updated	= datetimeField()



	#评论_表属性
	content = textField()




