# Reto 8
### Julian Jacobo Gustin Moreno

***

### 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
#Definir variables
n : int = 1

if __name__ == "__main__":
    for n in range(1, 101): #Iterar sobre los numeros del 1 al 100
        print(n) #Imprimir el numero
        print(f"El cuadrado de {n} es", (n**2)) #Imprimir el cuadrado del numero

```
***
### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
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
```

***
### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
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
```

***
### 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
# Definir variables
n = int(input("Ingrese un número natural: "))
i : int = 1
resultado = 1

if __name__ == "__main__":
    for i in range(1, (n+1)):
        resultado *= i #Multiplicar resultado por el numero actual
        print (f"{i}!={resultado}") #Imprimir numero y su factorial
```
***
### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
#Definir variables
n= int(input("Ingrese un número natural: "))
i : int = 1 
r : int = 1

if __name__ == "__main__":
    for i in range (n):  #Iterar hasta n-1
        r *= 2 #Multiplicar r por 2 en cada iteración
    print(f"2 elevado a {n} es igual a {r}")
```
***
### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
#Definir variables
x = float(input("Ingrese un número real(base): "))
n = int(input("Ingrese un número natural (potencia): "))
r : int = 1

if __name__ == "__main__": 
    for i in range (n):
        r *= x # Multiplicar x por r n veces
    print(f"{x} elevado a {n} es igual a {r}")
```
***
### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
#Definir variables
i : int = 1
t : int = 1
r : int = 1
if __name__ == "__main__": 
    for i in range (1,10): #Numeros del 1 al 9
        print(f"Tabla de {i}")
        for t in range (1,11): # Números del 1 al 10
            r = i*t # Multiplica los numeros i por los números t en cada iteración 
            print(f"{i} * {t} = {r}") 

```
***
### 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```
***
### 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

```python
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
```
### Disclaimer: Para las aproximaciones de series determine con que valor n se obtiene menos del 0.1% de error.

20 funciona bien para todos.

