#Definir variables
n= int(input("Ingrese un número natural: "))
i : int = 1 
r : int = 1

if __name__ == "__main__":
    for i in range (n):  #Iterar hasta n-1
        r *= 2 #Multiplicar r por 2 en cada iteración
    print(f"2 elevado a {n} es igual a {r}")
