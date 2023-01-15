#!/usr/bin/python3
data='''
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
      
            '''

data1='''
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
}'''
class style_handler:
	def __init__(self,log:object,args:object):
		self.val=args.theme
		self.fnm=args.css
		self.log=log
		self.args=args
		self.css_data=[]
		self.css_is_saved=[]
		if not self.args.debug:
			self.css_data.append(self.css())
	def get_root_dir(self) -> str:
		from appdirs import AppDirs
		dirs=AppDirs('bc03','flask_file_server')
		return dirs.user_data_dir
	#Saves the css data for future use
	def save_css_data(self,style:str) -> None:
		root=self.get_root_dir()
		if root:
			self.log.debug(f'Saving css data  to {root+self.fnm}')
			self.css_is_saved.append(True)
			try:
				from os import path,makedirs
				if not path.isdir(root):
					makedirs(root)
				with open(path.join(root,self.fnm),'w') as file:
					file.write(style)
			except Exception as e:
				self.log.error(f'Failed to save CSS "{self.fnm}" - {e}')
	#Opens the css file
	def open_file(self,notify=True) -> str:
		try:
			with open(self.fnm) as file:
				rp=(True,file.read())
			if self.args.save_css and not self.css_is_saved:
				self.save_css_data(rp[1])
		except Exception as e:
			if notify:
				self.log.error(f'Failed to open CSS file "{self.fnm}" - {e}')
			rp=(False,e)
		return rp
	#Opens previous saved data
	def open_cache(self):
		try:
			with open(self.get_root_dir()+'/'+self.fnm) as fp:
				return fp.read()
		except:pass
	#Main method
	def css(self) -> str:
		if self.css_data:
			return self.css_data[0]
		else:
			if self.fnm:
				cache=self.open_cache()
				if cache and not self.args.no_cache:
					self.log.debug(f'Serving css from cache of {self.fnm}')
					return cache
				fp=self.open_file()
				if fp[0]:
					return fp[1]
			css1={ 1 : data,2 : data1,}
			return css1[self.val]                                                                                  