import os
os.system('cls')
mensaje = "Fundamentos,"
""" consonantes = int(0)
vocales = int(0)
lstvocales = "aeiou".upper()
for caracter in mensaje:
    if caracter.upper() in lstvocales:
        vocales = vocales + 1
    elif caracter.isalpha():
        consonantes +=1
     
print (f"El total de vocales es = {vocales}")
print (f"El total de consonantes es = {consonantes}") """
for item in range(1,5,2):
    print(item)

for i,item in enumerate(mensaje):
    print(f"Pos {i} - {item}")
    mensaje = mensaje.replace(item,"-")
    print(mensaje)
    os.system("pause")

