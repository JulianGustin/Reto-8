import math 

# Definir e inicializar variables
x = float(input("Ingrese un número real: "))
n : int = 20
aprox = 0

# Definir función aproximación arcotangente
def aprox_arc(n, x):
    aprox = 0
    for i in range(n):
        # Definir las partes de la función
        c = (-1) ** i
        n = x ** (2 * i + 1)
        d = 2 * i + 1
        aprox += c * (n / d)  # Calcular valor aproximado usando serie de Maclaurin
    
    print(f"El valor aproximado es {aprox}")
    
    valor_real = math.atan(x)  # Calcular valor real de la función
    print("El valor real de la función arcotangente es:", valor_real)
    print(f"La diferencia es de {abs(aprox - valor_real)}")  # Calcular la diferencia
    


if __name__ == "__main__":
    aprox_arc(n, x)