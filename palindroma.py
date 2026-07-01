'''
Una stringa si dice "palindroma" se resta uguale sia se letta da 
sinistra verso destra che da destra verso sinistra (ignorando spazi e 
punteggiatura).

Ad esempio, la stringa seguente è palindroma:

Ed Irene se ne ride.

Scrivere un programma che, letta una stringa 'string' da tastiera, 
verifichi se la stringa è palindroma, ignorando eventuali spazi e 
caratteri di punteggiatura.

Organizzare il programma in opportune funzioni che effettuino il calcolo.
'''
import sys

def lowercaps_removeSpace(frase):
    result = frase.replace(" ", "")
    result = result.replace(".","")
    result=result.lower()
    return result
    

def palindroma(frase)-> bool:
    result=lowercaps_removeSpace(frase)
    print(result)
    puntatore_sinistra=0
    puntatore_destra=len(result)-1
    while puntatore_destra >= puntatore_sinistra :
        print(f"{result[puntatore_destra]} - {result[puntatore_sinistra]}")
        if result[puntatore_sinistra] != result [puntatore_destra]:
            print ("la frase non è palindroma")

            return False
        puntatore_destra-=1
        puntatore_sinistra+=1

    print("la frase è palindroma")
    return True

def palindroma_substring(frase) -> str:

    result=""
    temp=""
    palindroma=lowercaps_removeSpace(frase)
    print(palindroma)
    puntatore_sinistra=0
    puntatore_destra=len(palindroma)-1
    while puntatore_destra >= puntatore_sinistra :
        print(f"{palindroma[puntatore_destra]} - {palindroma[puntatore_sinistra]}")
        if palindroma[puntatore_sinistra] != palindroma [puntatore_destra]:
            if len(temp) > len(result):
                result = temp
            temp=""
        else:
            temp+=palindroma[puntatore_sinistra]
            if puntatore_destra != puntatore_sinistra:
                temp+=palindroma[puntatore_destra]
        
        puntatore_destra-=1
        puntatore_sinistra+=1

    if len(temp) > len(result):
        result=temp
    print(result)
    return result
    


def main():
    frase=input("inserisci la frase! ")
    palindroma(frase)
    print(palindroma_substring(frase))
    return 0

if __name__ == "__main__":
    sys.exit( main() )
