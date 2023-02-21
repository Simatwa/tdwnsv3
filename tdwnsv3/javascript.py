"""'
MIT License

Copyright (c) 2023 Simatwa Caleb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


class data:
    def __init__(self, args: object):
        self.args = args
        self.data = """
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
                        find[i].style.display='%s';
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
	
	""" % (
            "inline-block" if self.args.theme == 3 else "list-item"
        )
