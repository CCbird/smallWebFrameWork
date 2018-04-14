function Submit(){

				var form = document.getElementById('blogpost_form');
				var elements = new Array();  

				var tagElements = form.getElementsByTagName('h1');  
				    for (var j = 0; j < tagElements.length; j++){ 
				       elements.push(tagElements[j]); 
				    } 

				var tagElements = form.getElementsByTagName('input');  
				    for (var j = 0; j < tagElements.length; j++){ 
				       elements.push(tagElements[j]); 
				    } 			    
				var tagElements = form.getElementsByTagName('textarea');  
				    for (var j = 0; j < tagElements.length; j++){ 
				       elements.push(tagElements[j]); 
				    }   
				
				if(elements[0].value.length==0){
					alert('标题不能为空');
					return false;
				}
				if(elements[1].value.length==0){
					alert('时间戳不能为空');
					return false;
				}
				if(elements[2].value.length==0){
					alert('内容不能为空');
					return false;
				}	
				
				form.submit();      	
				alert("提交成功！！"); 
	

				

				
	}