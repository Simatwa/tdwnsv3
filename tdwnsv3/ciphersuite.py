from cryptography.fernet import Fernet
class encryption:
	def __init__(self,key:bytes,args:object,config:dict):
		self.args=args
		self.config=config
		self.__fernet=Fernet(key)
	#Encrypts the data 
	def encrypt(self,text:str) -> str:
		return self.__fernet.encrypt(text.encode()).decode()
	#Decrypts the data
	def decrypt(self,text:str) -> str:
		try:
			text=text.encode()
			decr=self.__fernet.decrypt(text).decode()
			rp=(True,decr)
		except Exception as e:
			rp=(False,e)
		return rp
	#Main method
	def handle_cipher(self,text,enc=False,dec=False,path=False):
		if self.args.encrypt:
			if enc:
				rp=(True,'/'+self.config['home']+'/'+self.encrypt(path))
			else:
				rp=self.decrypt(text)
		else:
			rp=(True,text)
		return rp
if __name__=='__main__':
	key=Fernet.generate_key()
	ciph=encryption(key)
	msg='Hello world'
	for _ in range(4):
		enc=ciph.encrypt(msg)
		dec=ciph.decrypt(enc)
		print(enc,dec)
		
#020123191601		