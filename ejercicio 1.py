numero1 = int(input("Escriba un número: "))
numero2 = int(input(f"Escriba un número mayor que {numero1}: "))
while numero2 <= numero1:
        numero2 = int(input(f"{numero2} no es mayor que {numero1}. Inténtelo de nuevo: ")
        )
print()
print(f"Los números que ha escrito son {numero1} y {numero2}.")
