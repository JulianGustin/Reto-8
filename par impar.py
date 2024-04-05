#Definir variables
i : int = 1
p : int = 2

if __name__ == "__main__":
    print("Lista de números impares de 1 a 999")
    for i in range(1, 1000, 2): #Inicia en 1, termina en 999 de 2 en 2
        print (i)
    print("Lista de números pares de 2 a 1000") 
    for p in range(2, 1001, 2): #Inicia en 2, termina en 1000 de 2 en 2
        print (p)