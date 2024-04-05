#Definir variables
n : int = 1

if __name__ == "__main__":
    for n in range(1, 101): #Iterar sobre los numeros del 1 al 100
        print(n) #Imprimir el numero
        print(f"El cuadrado de {n} es", (n**2)) #Imprimir el cuadrado del numero