
#ZADATCI(riješite, dokumentirajte I zatim pročitajte docstring): 
#Kreirajte funkciju koja računa zbroj svih znamenaka nekog cijelog broja 
def zbroj(n):
    '''opis funkcije'''
    L=list(str(n))
    b=0
    for i in L:
        b+=int(i)
    return b
x=int(input('upisi cijeli broj:'))
print(zbroj(x))    