text = "Studenti_kybernetiky_jsou_rádi,_když_mají_3_testy_v_jedné_hodině"
while True:

    for i in range(4,65,15):
        u=5
        if(u==5):
            print(text[i-4] + text[i-3] + text[i-2] + text[i-1] + text[i])
        u -= 1
        if(u==4):
            i += 5
            print(text[i-4] + text[i-3] + text[i-2] + text[i-1])
        u -= 1
        if(u==3):
            i += 4
            print(text[i-4] + text[i-3] + text[i-2])
        u -= 1
        if(u==2):
            i += 3
            print(text[i-4] + text[i-3])
        u -= 1
        if(u==1):
            i += 2
            print(text[i-4])
    break
