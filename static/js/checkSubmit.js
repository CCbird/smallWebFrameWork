

var checkSubmitFlag = false;

function checkSubmit(){

	if(checkSubmitFlag == true){

		return false;
}		


	checkSubmitFlag = true;
	return true;
}


document.onclick=

function doconclick(){

	if(checkSubmitFlag){
		window.event.returnValue =false;
	}

}
<form method="post" onsubmit="return checkSubmit();"> 
