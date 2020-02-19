        var tim;
        var f = new Date();
        var min = document.getElementById("myVar1").value;
        var sec = document.getElementById("myVar2").value;


//        alert(min)
function customSubmit(someValue){

        	 document.questionForm.minute.value = min;
        	 document.questionForm.second.value = sec;
//        	 document.questionForm.submit();
//        	 var q1=document.forms["questionForm"]["q1"].value;
//        	 alert(q1);

//        	 document.getElementById("alert").innerHTML=document.forms["questionForm"]["q1"].value;


        	 }
     examTimer();
     function examTimer() {

        if (parseInt(sec) >0) {

			    document.getElementById("demo").innerHTML = "Time Remaining "+min+" : " + sec;
                sec = parseInt(sec) - 1;
                tim = setTimeout("examTimer()", 1000);
            }
        else {
                   if (parseInt(min)==0 && parseInt(sec)==0){
			    	document.getElementById("demo").innerHTML = "Time Remaining "+min+": " + sec;
				     alert("Time Up");
				     document.questionForm.minute.value=0;
				     document.questionForm.second.value=0;
				     document.questionForm.submit();
			         }


            if (parseInt(sec) == 0) {

				            document.getElementById("demo").innerHTML = "Time Remaining "+min+" : " + sec;
                    min = parseInt(min) - 1;

					                     sec=59;

                    tim = setTimeout("examTimer()", 1000);
            }

        }


     }

function noBack()
{
// return "You work will be lost.";
//window.open ("https://viralpatel.net/blogs/","mywindow","status=1,toolbar=0");
window.history.forward(1);
setTimeout("noBack()",0);
}