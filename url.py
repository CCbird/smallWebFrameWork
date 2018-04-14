# -*- coding: UTF-8 -*-
'''
urls = [('^/index$'                    ,     'index'),
        ('^/admin$'             	   ,	 'admin'),
        ('^/admin/post.html$'          , 	 'ADD'  ),
        ('^/static/css/add.css$' 	   ,  	 'css'  ),
        ('^/static/css/admin.css$' 	   ,  	 'css'  ),
        ('^/admin/add.html$'           ,     'ADD'  ),
        ('^/static/js/getTimeStamp.js$',     'js'   ),
        ('^/static/img/1.jpeg$'        ,     'jpeg' ),
        ('^/static/js/Submit.js$' ,     'js'   )   
       ]
'''

d_urls      = [ ('^/index$'                    ,      'index'),
		        ('^/admin$'             	   ,	  'admin'),
		        ('^/admin/add.html$'           ,      'ADD'  ),
		        ('^/admin/post.html$'          , 	  'ADD'  )
		      ]

static_urls = [ ('^/static/css/add.css$' 	   ,  	 'css'  ),
		        ('^/static/css/admin.css$' 	   ,  	 'css'  ),
		        ('^/static/js/getTimeStamp.js$',     'js'   ),
		        ('^/static/js/Submit.js$'      ,     'js'   ),
		        ('^/static/img/1.jpeg$'        ,     'jpeg' )   
		       ]

urls = d_urls + static_urls






'''
('^/static/img/*.png$','png'),
('^/static/img/*.gif$','gif'),
('^/static/css/*.css$','css')]
'''
