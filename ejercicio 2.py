primero = float(input("Escriba un número: "))
segundo = float(input(f"Escriba un número mayor que {primero}: "))

while segundo > primero:
    segundo = float(input(f"Escriba un número mayor que {primero}: "))

print()
print(f"{segundo} no es mayor que {primero}.")