import numpy as np

cislo_hadane = np.random.randint(1,20)
pokusy = 0
while(True):
    cislo_x = input("hadej cislo: ")
    try:
        cislo = int(cislo_x)
        if(cislo == cislo_hadane):
            print("spráně!!")
            print("travlo to pokusů: " + str(pokusy))
            break
        elif(cislo<cislo_hadane):
            print("špatně, hádej vyšší")
            pokusy += 1
        elif(cislo>cislo_hadane):
            print("špatně, hádej nížš")
        pokusy += 1
    except:
        print("nezadal jsi číslo")