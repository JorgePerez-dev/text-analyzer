texto =  input("introduzca un texto cualquiera: ")
tres_letras = input("Ahora introduce tres letras: ")



texto = texto.lower()
tres_letras = tres_letras.lower()

print("A continuacion salen las veces que aparecen cada letra: ")
print(f"La letra '{tres_letras[0]}' aparece {texto.count(tres_letras[0])} veces.")
print(f"La letra '{tres_letras[1]}' aparece {texto.count(tres_letras[1])} veces.")
print(f"La letra '{tres_letras[2]}' aparece {texto.count(tres_letras[2])} veces.")


print("A continuación las palabras totales que hay en un texto son: ")

largo = texto.split()
print(f"el largo de {texto} es de {len(largo)}")


print("\n")
print("A continuación vamos a sacar la primera y ultima letra de tu texto")
print(f"la primera letra es {texto[0]} y la ultima es {texto[-1]}")

print("\n")
print("A continuación vamos a invertir tu texto")
invertir = texto[::-1]
print(invertir)


print("\n")
buscar = "python"  in texto
print(f"La palabra Python te va a decir 'True' si esta en el texto o 'False' si no esta en el texto: {buscar}")


