import re

class Targa(str):
	def __new__(cls, t:str):
		if t is None:
			raise ValueError("La targa è none")
		t = t.upper().replace(" ","")
		if not re.fullmatch('[A-Z]{2}[0-9]{3}[A-Z]{2}',t):
			raise ValueError(f"Targa invalida")
		return super().__new__(cls,t)

class Telefono(str):
	def __new__(cls, n:str):
		if n is None:
			raise ValueError("Il telefono è none")
		n = n.replace(" ","")
		if not re.fullmatch('\\+?[0-9]{0,15}',n):
			raise ValueError(f"Telefono incorretto")
		return super().__new__(cls)  


class CodiceFiscale(str):
	def __new__(cls, c:str):
		if c is None:
			raise ValueError("Il codice fiscale è none")
		c = c.strip().upper()
		if not re.fullmatch('[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[0-9A-Z]{4}[A-Z]',c):
			raise ValueError(f"Codice Fiscale incorretto")
		return super().__new__(cls) 
			



class Indirizzo:
	__via:str 
	__civico:str
	__cap:str 
	def __init__(self, via:str, civ:str,cap:str):
		if via is None:
			raise ValueError("La via è none")
		if civ is None:
			raise ValueError("Il civico è none")
		if cap is None:
			raise ValueError("Il cap è none")

		self.__via = via 
		if not re.fullmatch('[0-9]+(/[a-zA-Z]+)?',civ):
			raise ValueError("Errore nel civico")
		self.__civico = civ
		if not re.fullmatch('[0-9]{5}',cap):
			raise ValueError("Errore nel cap")
		self.__cap=cap

	def __str__(self):
		return f"via:{self.__via} civico:{self.__civico} cap:{self.__cap}"

	def getVia(self)->str:
		return self.__via

	def getCivico(self)->str:
		return self.__civico

	def getCap(self)->str:
		return self.__cap
	def __hash__(self)->int:
		return hash( (self.getVia(), self.getCivico(), self.getCap() ) )  
	def __eq__(self, other:any)->bool:
		if not isinstance(other, type(self)) or hash(self) != hash(other):
			return False 
		return (self.getVia(), self.getCivico(), self.getCap() ) == (other.getVia(), other.getCivico(),other.getCap() )

