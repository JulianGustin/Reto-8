import math 
import funcion_factorial

# Definir e inicializar variables
x = float(input("Ingrese un número real: "))
n : int = 20
valor_real = math.exp(x)  # Calcular valor real de la función
    
# Definir funcion aproximación
def aprox_exponencial(n:int, x:float):
    aprox = 0
    for i in range(n):
        aprox += (x**i) / funcion_factorial.factorial(i)  # Calcular valor aproximado usando serie de Maclaurin
    print(f"El valor aproximado es {aprox}")
    
    print("El valor real de la función exponencial es: ", valor_real)
    if aprox > valor_real:
        print(f"La diferencia es de {aprox - valor_real}")  # Calcular la diferencia
    else:
        print(f"La diferencia es de {valor_real - aprox}")



if __name__ == "__main__":
    aprox_exponencial(n,x)


    
    
