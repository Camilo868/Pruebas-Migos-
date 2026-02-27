
## Sprint 1: Registro inicial

# personas=int(input("Ingrese el numero de personas que van a ingresar: "))

# for i in range (personas):
#     print("pass")

## sprint 2: registro por participante.

# print("Bienvenido a mi programa pa saber si cumples los requisitos")
# personas=int(input("Ingrese el numero de personas que van a ingresar: "))

# for i in range (personas):
#     persona=(input("Ingrese nombre: "))
#     edad=int(input("Ingrese edad: "))
#     conocimiento=input("Tiene conocimientos basicos de computacion(SI/NO): ").lower()

## Sprint 3: Reglas para aceptar rechazar
#
#     if edad >= 15 and conocimiento == ("si"):
#         print("Puede participar en el taller")
#     else:
#         print("No comples los requisitos imbecil")
#
## Sprint 4: Validación de errores.

print("Bienvenido a mi programa pa saber si cumples los requisitos")
personas=int(input("Ingrese el numero de personas que van a ingresar: "))

for i in range (personas):
    persona=(input("Ingrese nombre: "))
    edad=input("Ingrese edad: ")
    while not edad.isdigit():
        print("Ingrese un valor entero")
        edad=input("Ingrese edad: ")

    conocimiento=input("Tiene conocimientos basicos de computacion(SI/NO): ").lower()
    if edad >= "15" and conocimiento == ("si"):
        print("Puede participar en el taller")
    else:
        print("No comples los requisitos imbecil")

##Sprint 5: Mensaje final

print("Proceso terminado")

