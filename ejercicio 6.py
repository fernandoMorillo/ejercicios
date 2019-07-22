'''Escriba un programa que pida el año actual y un año cualquiera 
y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.'''

fecha_1 = int(input("¿En qué año estamos?: "))
fecha_2 = int(input("Escriba un año cualquiera: "))

if fecha_1 > fecha_2:
    print(f"Desde el año {fecha_2} han pasado {fecha_1 - fecha_2} años.")
elif fecha_1 < fecha_2:
    print(f"Para llegar al año {fecha_2} faltan {fecha_2 - fecha_1} años.")
else:
    print("¡Son el mismo año!")