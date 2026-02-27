import numpy as np

def druhe_nejvetsi(seznam):
    if seznam[0] > seznam[1]:
        max = seznam[0]
        druhe = seznam[1]
    else:
        max = seznam[1]
        druhe = seznam[0]
    for i in range(len(seznam)):
        if (seznam[i] > max):
            druhe = max
            max = seznam[i]
        if (seznam[i]>druhe and seznam[i]!=max):
            druhe = seznam[i]
    return druhe

x = [12,54,1,34,25]
druhe = druhe_nejvetsi(x)
print(druhe)

def prvocislo(a):
    if (a<2):
        print(str(a) + " není prvočíslo")
        return False
    for i in range(2,int(a** (1/2)+1)):
        if(a%i==0 ):
            print( str(a) + " není prvočíslo")
            return False

    print( str(a) + " je prvočíslo")
    return True

while(True):
    cislo = input("napiš číslo: ")
    try:
        zadane = int(cislo)
        break
    except:
        print("nezadal jsi číslo zadej znovu")

prvocislo(zadane)

