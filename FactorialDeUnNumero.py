fact = 1
num = int(input("Ingrese el nùmero: "))
#es necesario un ciclo para que haga las iteraciones
for i in range (1, num + 1):
# se define i como variable de iteracion y se le asigna un rango 
#se asigna +1 porque el ciclo llegue hasta un numero antes 
    fact*=i
#se hace esto para que se multipliquen los valores mientras el ciclo hace las iteraciones
print ("El factorial de ", num , "es: " ,fact)