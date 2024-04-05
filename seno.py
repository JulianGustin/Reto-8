import math 
import funcion_factorial

# Definir e inicializar variables
x = float(input("Ingrese un número real: "))
n : int = 20
aprox : float = 0

# Definir funcion aproximación seno
def aprox_seno(n, x):
    aprox = 0
    for i in range(n):
        #Definir las partes de la función
        c = (-1)**i
        n = x**(2*i+1)
        d = funcion_factorial.factorial(2*i+1)
        aprox += c * (n/d)  # Calcular valor aproximado usando serie de Maclaurin
    print(f"El valor aproximado es {aprox}")
    
    valor_real = math.sin(x)  # Calcular valor real de la función
    print("El valor real de la función seno es: ", valor_real)
    print(f"La diferencia es de {abs(aprox - valor_real)}")  # Calcular la diferencia

if __name__ == "__main__":
    aprox_seno(n,x)



