num = int(input("ingrese el numero: "))
a = 1
b = 0
while a <= num :
    if num % a == 0 :
        b = b + 1
    a = a + 1
if b == 2 : 
        print ("el numero", num, "es primo")
else : print("el numero", num, "no es primo")
