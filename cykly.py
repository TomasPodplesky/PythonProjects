print("tenhle python vypíše ahoj podle proměnné které napíšete")
vstup = input("Zadej cislo: ")
try:
    A = int(vstup)
except:
    A = 1
B = input("sem zadej do kolika pocitat(cislo): ")
try:
    B = int(B)
except:
    B = 1
for i in range(A, B):
    print(i)
    print("ahoj")
print("*****")
for x in range(17, 13, -1):
    print(x)
print("****")
for y in range(0, 10, 1):
    print(y/10)
print("*******")
for z in range(0, 4):
    print(z*2)
print("*******")
for b in range(0, 11, 2):
    print(b)
print("*******")
for i in range(0, 11):
    if i%2==0:
        print(i)
print("****")
for i in range(5):
    for j in range(5):
        print(str(i)+ "," str(j))