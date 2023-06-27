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
data = """
h1{
       height:auto;
        color:yellow;
        font-size:110%;
        text-align:center;
        font-weight:bold;
        position:sticky;
        background-color:purple;
        border-radius:10px;
        top:0;
        padding:20px;
        margin-left:0;
        margin-right:0;
    }
    
     body{
            background-color:pink;
            font-family:garamond;
            text-align:center;
            }
            
            
       a{
              text-decoration:none;
            }
            
        footer{
         background-color:black;
         color:lime;
         border:5px solid black;
         border-radius:30px;
         text-align:center;
         padding:20px;
         bottom:0;
         }
         
   .folders{
        background-color:darkGray;
        border-radius:1px solid blue;
        padding:10px;
        }
        
    li{
           display:-webkit-inline-box;
            color:lime;
            }
            
    a.file{
          color:blue;
          }
          
     a.dir{
          color:black;
          font-weight:bold;
          font-family:sans-serif;         
          }
          
    li.doc{
           text-align:center;
           color:green;
           background-color:orange;
           padding:10px;
           border-radius:10px;
           margin:7px;
           }
           
video{
      border:5px solid lime;
      border-radius:13px;
      color:mediumTurquoise;
      background-color:orange;
      }
      
 img,.pic,.vida,.aud,video,.header,.file,audio,#cp{
      max-width:100%;
      min-width:100%;
      text-align:center;
      
        }
        
     .header{
       color:red;
       font-weight:bold;
       font-size:180%;
       padding:10px;
       text-decoration:underline;
       }
       
       
.doc{
     color:fuchsia;
     }
     
.aud{
     background-color:darkblue;
     padding:5px;
     border-radius:8px;
     margin-top:5px;
     }
     
#cp{
    text-align:center;
    background-color:cornsilk;
    color:Red;
    font-size:110%;
    height:1.0cm;
    border-radius:50px;
    font-family:didot;
    text-decoration:bold;
    }
    
button{
    background-color:cyan;
    font-weight:bold;
    height:30px;
    }
    
h4{
    color:darkBrown;
    }
    
form{
        text-align:center;
    }
  
marquee{
        font-size:55%;
    }
    
a.but{
        color:red;
        border:1px solid blue;
        background-color:lime;
        border-radius:20px;
        padding:2px;
        font-size:15px;
        font-family:verdana;
    }
      
            """

data1 = """
body{
    background-color:antiquewhite;
    text-align:center;
    font-family:'Times New Roman', Times, serif;

}

h1{
    position:sticky;
    top:0;
    margin-left:0;
    margin-right:0;
    padding:20px;
    background-color:blueviolet;
    clear:both;
    font-size:110%;
    
}

.header{
    color:orangered;
    text-decoration:underline;
}

a{
    text-decoration:none;
}

div.folders{
    background-color:aliceblue;
    padding:5px;    
}

button{
    background-color:indianred;
    margin:3px;
    font-size:100%;
}

.dir{
    color:chartreuse;
    font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
    font-weight:bold;
}

#cp{
      background-color:blanchedalmond;
      width:60%;
      font-size:80%;
      border-radius:20px;
      font-family:'Courier New', Courier, monospace;
      padding:10px;
      color:blueviolet;
}

input#cp{
    text-align:center;
    padding:10px;
    height:0.2cm;
}

.vida{
    display:inherit;
    margin:5px;
}
  
p.doc{
    display:inherit;
    color:indigo;
    font-family:verdana;
}

video{
    border:2px solid salmon;
    background-color:black;
    border-radius:15px;
}

img,video{
    height:auto;
    width:340px;
    
}

audio{
    height:1cm;
    width:90%;
    }
    
.aud{
    background-color:lightGray;
    color:indigo;
    padding:10px;
    margin-top:10px;
}

li.doc{
    display:-webkit-inline-box;
    color:blue;
    background-color:burlywood;
    padding:10px;
    border-radius:10px;
    margin:7px;
    font-family:verdana;
    justify-items:flex-start;
}

.but{
    background-color:antiquewhite;
    padding:4px;
    border-radius:8px;
}

marquee{
    margin:5px;
    font-family:'Courier New';
    font-size:55%;
}

footer{
    margin-top:auto;
    background-color:lightseagreen;
    padding:10px;
    bottom:0;
}"""

data2 = """
body{
    background-color: #f2f2f2;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    text-align:center;
    
}

h1{
    position:sticky;
    top:0;
    margin-left:0;
    margin-right:0;
    padding:20px;
    background-color:#fff;
    clear:both;
    font-size:1.6rem;
    border-bottom: 1px solid #ddd;
}

.header{
    color: #222;
    text-decoration: none;
}

a{
    text-decoration:none;
}

div.folders{
    background-color: #fff;
    padding: 10px;
    border: 1px solid #ddd;
}

button{
    background-color: #f2f2f2;
    margin: 5px;
    font-size: 14px;
    border: 1px solid #ddd;
    padding: 8px 16px;
    border-radius: 4px;
}

.dir{
    color: #222;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    font-weight: bold;
}

.dir:hover{
    background-color:blue;
    color:white;
    }

#cp{
    background-color: #fff;
    width: 60%;
    font-size: 16px;
    border-radius: 20px;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    padding: 10px;
    color: #222;
    border: 1px solid #ddd;
    /* display:none; */
}

input#cp{
    text-align: center;
    padding: 10px;
    height: 0.2cm;
}

input#cp:focus{
   height:0.8cm;
   border:1px solid blue;
 }

.vida,.pic,.aud{
    display: inline-block;
    margin: 5px;
    max-width: 320px;
}

p.doc{
    display: inline-block;
    color: #222;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    max-width: 340px;
}

/*
.vida{
    max-width:320px;

} */

video{
    border:none;
    background-color: 000;
    border-radius: 4px;
    width: 100%;
    height: auto;
}

img, video{
    max-width:100%;
    height: auto;
    
}

audio{
    height: 50px;
    width:100%;
}

.aud{
    background-color: #fff;
    color: #222;
    padding: 10px;
    margin-top: 10px;
    border: 1px solid #ddd;
    min-width:300px;
    max-width:300px;
}

li.doc{
    display: inline-block;
    color: #222;
    background-color: #fff;
    padding: 10px;
    border-radius: 4px;
    margin: 7px;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.but{
    background-color: #fff;
    padding: 4px;
    border-radius: 8px;
}

marquee{
    margin:5px;
    font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;
    font-size:14px;
    color:#222;
}

footer{
  /*  position: fixed; */
    bottom: 0;
    width: 100%;
    background-color: #f2f2f2;
    padding: 10px;
    color: #666;
    text-align: center;
    font-size: 14px;
    border-top: 1px solid #ddd;
}
"""
data3 = """

body{
    background-color: #f2f2f2;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    text-align:center;
    
}

h3{
 background-color:red;
 color:lime;
 padding:5px;
 margin-left: 30%;
 margin-right: 30%;
 border-radius:2px;
}

p.nav{
    position:sticky;
    top:0;
    margin-left:0;
    margin-right:0;
    padding:20px;
    background-color:#fff;
    clear:both;
    font-size:1.6rem;
    border-bottom: 1px solid #ddd;
}

.header{
    color: #222;
    text-decoration: none;
}

a{
    text-decoration:none;
}

a.listed_dir{
 background-color:blue;
 padding:5px;
 border-radius:10px;
 color:lightgreen;
 font-size:20px;
}

div.folders{
    background-color: #fff;
    padding: 10px;
    border: 1px solid #ddd;
}

button{
    background-color: lightgreen;
    margin: 5px;
    font-size: 14px;
    border: 1px solid #ddd;
    padding: 8px 16px;
    border-radius: 4px;
}

.dir{
    color: #222;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    font-weight: bold;
}

a.dir{
  color : black;
}

a.file{
  color:darkgreen;
  
}

/*button > a.dir:hover*/
button:hover, a.dir:hover{
    background-color:yellow;
    color:red;
    }

#cp{
    background-color: #fff;
    width: 60%;
    font-size: 16px;
    border-radius: 20px;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    padding: 10px;
    color: #222;
    border: 1px solid #ddd;
    /* display:none; */
}

input#cp{
    text-align: center;
    padding: 10px;
    height: 0.2cm;
}

input#cp:focus{
   height:0.8cm;
   border:1px solid blue;
 }

.vida,.pic,.aud{
    display: inline-block;
    margin: 5px;
    max-width: 320px;
}

p.doc{
    display: inline-block;
    color: #222;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    max-width: 340px;
}

/*
.vida{
    max-width:320px;

} */

video{
    border:none;
    background-color: 000;
    border-radius: 4px;
    width: 100%;
    height: auto;
}

img, video{
    max-width:100%;
    height: auto;
    
}

audio{
    height: 50px;
    width:100%;
}

.aud{
    background-color: #fff;
    color: #222;
    padding: 10px;
    margin-top: 10px;
    border: 1px solid #ddd;
    min-width:300px;
    max-width:300px;
}

li.doc{
    display: inline-block;
    color: #222;
    background-color: #fff;
    padding: 10px;
    border-radius: 4px;
    margin: 7px;
    font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.but{
    background-color: #fff;
    padding: 4px;
    border-radius: 8px;
}

marquee{
    margin:5px;
    font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;
    font-size:14px;
    color:#222;
}

footer{
  /*  position: fixed; */
    bottom: 0;
    width: 100%;
    background-color: #f2f2f2;
    padding: 10px;
    color: #666;
    text-align: center;
    font-size: 14px;
    border-top: 1px solid #ddd;
    /*margin-top:100vh;*/
}
"""


class style_handler:
    def __init__(self, log: object, args: object):
        self.val = args.theme
        self.fnm = args.css
        self.log = log
        self.args = args
        self.css_data = []
        self.css_is_saved = []
        if not self.args.debug:
            self.css_data.append(self.css())

    def get_root_dir(self) -> str:
        from appdirs import AppDirs

        dirs = AppDirs("bc03", "flask_file_server")
        return dirs.user_data_dir

    # Saves the css data for future use
    def save_css_data(self, style: str) -> None:
        root = self.get_root_dir()
        if root:
            self.log.debug(f"Saving css data  to {root+self.fnm}")
            self.css_is_saved.append(True)
            try:
                from os import makedirs, path

                if not path.isdir(root):
                    makedirs(root)
                with open(path.join(root, self.fnm), "w") as file:
                    file.write(style)
            except Exception as e:
                self.log.error(f'Failed to save CSS "{self.fnm}" - {e}')

    # Opens the css file
    def open_file(self, notify=True) -> str:
        try:
            with open(self.fnm) as file:
                rp = (True, file.read())
            if self.args.save_css and not self.css_is_saved:
                self.save_css_data(rp[1])
        except Exception as e:
            if notify:
                self.log.error(f'Failed to open CSS file "{self.fnm}" - {e}')
            rp = (False, e)
        return rp

    # Opens previous saved data
    def open_cache(self):
        try:
            with open(self.get_root_dir() + "/" + self.fnm) as fp:
                return fp.read()
        except:
            pass

    # Main method
    def css(self) -> str:
        if self.css_data:
            return self.css_data[0]
        else:
            if self.fnm:
                cache = self.open_cache()
                if cache and not self.args.no_cache:
                    self.log.debug(f"Serving css from cache of {self.fnm}")
                    return cache
                fp = self.open_file()
                if fp[0]:
                    return fp[1]
            css1 = {
                1: data,
                2: data1,
                3: data2,
                4: data3,
            }
            return css1[self.val]
