import numpy as np

for i in range(10):
    cislo_hadane = np.random.randint(1,20)

while(True):
    cislo_x = input("hadej cislo: ")
    cislo = int(cislo_x)
    if(cislo == cislo_hadane):
        print("spráně!!")
        break
    elif(cislo<cislo_hadane):
        print("špatně, hádej vyšší")
    elif(cislo>cislo_hadane):
        print("špatně, hádej nížš")
