function checkMe()
{
var str = document.getElementsByName("box");
var objarray = str.length;
var con = [];
var del_id = [];


	for (i = 0; i < objarray; i++) {
	    if (str[i].checked == true) {
	        con.push("chk_"+str[i].id);       
	    }
	        
	}

	console.log(con);

	for (j=0;j<con.length;j++){
		del_id.push(document.getElementsByName(con[j]));		
	}

	for (k=0;k<del_id.length;k++){
		console.log(del_id[k][0].id);
	}
	

}

function Delete(){
	var str = document.getElementsByName("box");
	var objarray = str.length;
	var con = [];
	var del_id = [];


	for (i = 0; i < objarray; i++) {
	    if (str[i].checked == true) {
	        con.push("chk_"+str[i].id);       
	    }
	        
	}

	//console.log(con);

	for (j=0;j<con.length;j++){
		del_id.push(document.getElementsByName(con[j]));		
	}

	for (k=0;k<del_id.length;k++){
		console.log(del_id[k][0].id);
		document.getElementById('ID').value = del_id[k][0].id;
		var form = document.getElementById('del_id'); 
		form.submit()
	}

	
	

}

