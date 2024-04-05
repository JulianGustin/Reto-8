#Definir variables
n = int(input("Ingrese un número natural mayor a 2: "))
if n < 2:
    print("Su número es menor a 2.")

i : int = 1



if __name__ == "__main__":
    if n % 2 == 0: #Para n par
        for i in range(n, 1, -2): #Rango desde n hasta 1 (sin contar el 1) restando 2 en cada iteración
            print(i)
    else: 
        for i in range((n-1), 1, -2): #Restar 1 a n para que sea par
            print(i)