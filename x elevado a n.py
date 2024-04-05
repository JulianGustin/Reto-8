#Definir variables
x = float(input("Ingrese un número real(base): "))
n = int(input("Ingrese un número natural (potencia): "))
r : int = 1

if __name__ == "__main__": 
    for i in range (n):
        r *= x # Multiplicar x por r n veces
    print(f"{x} elevado a {n} es igual a {r}")