'''Escriba un programa que pida un valor límite positivo y a continuación pida números 
hasta que la suma de los números introducidos supere el límite inicial.  '''

def bienvenida(): 
        
    print("Bienvenidos...")
    print("A continuación Escriba un valor para darle limite al programa")
    print("Luego, digite números que llevarán al acumulado que dio al principio")

def datos():
    suma = 0
    valor = float(input("Ingrese el valor límite: "))
    while valor <= 0:
        valor = float(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))

    print()
    numero = float(input("Escriba un número: "))
    suma = numero 

    while suma < valor:
        numero = float(input("Escriba otro número: "))
        suma += numero  
    if suma == valor:    
        print()
        print(f"La suma de los números introducidos es {suma}.")
    else:
        print(f"Ha superado el límite. La suma de los números introducidos es {suma}.")
        print(f"Y el valor límite es {valor}.")
    

bienvenida()
datos()