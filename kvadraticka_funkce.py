
def kvadr(a,b,c):
    D = pow(b,2)-4*a*c
    if(D>0):
        x1 = (-b+pow(D,1/2))/(2*a)
        x2 = (-b-pow(D,1/2))/(2*a)
        vysledek = print("řešení jsou, x1: " + str(x1) + " x2: " + str(x2))
    elif(D<0):
        x1 = (-b+pow(D,2))/2*a
        vysledek = print("řešení je: " +str(x1))
    elif(D==0):
        vysledek = print("nemá řešení")
    return vysledek

kvadr(1,3,1)
