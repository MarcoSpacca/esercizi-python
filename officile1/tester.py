from main import *
import sys

def main():
	targa = Telefono("+39329")
	targa2 = Telefono("+39329")
	print (targa == targa2)

if __name__=="__main__":
	sys.exit(main())