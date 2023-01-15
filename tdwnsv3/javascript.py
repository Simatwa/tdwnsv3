data="""
 function query()
 {
       let input=document.getElementById('cp').value;
       input=input.toLowerCase();
       let find=document.getElementsByClassName('vida');
        for(i=0;i<find.length;i++)
               {
                if(!find[i].innerHTML.toLowerCase().includes(input))
                     {
                      find[i].style.display='none'; 
                      }
               else {
                        find[i].style.display='list-item';
                      } 
                 } 
    }
   
   
function refresh()
      {
			window.location.reload();
		}
		

function notify()
     {
			var file = document.getElementById('bin').value;
			if (file){
				alert('Uploading file! Wait for response.');
			}
			else{
				alert('Kindly choose a file to upload!');
				return false;
			}
	}
	
	"""