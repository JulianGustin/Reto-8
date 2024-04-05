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