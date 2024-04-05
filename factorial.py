# Definir variables
n = int(input("Ingrese un número natural: "))
i : int = 1
resultado = 1

if __name__ == "__main__":
    for i in range(1, (n+1)):
        resultado *= i #Multiplicar resultado por el numero actual
        print (f"{i}!={resultado}") #Imprimir numero y su factorial