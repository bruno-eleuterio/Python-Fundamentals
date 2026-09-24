nome = "pYthOn"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá Mundo!     "
print(texto.strip() + ".")
print(texto.lstrip()+ ".")
print(texto.rstrip()+ ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14,"#"))
print("P-y-t-h-o-n")
print("-".join(menu))

print()

for letra in menu:
    print(letra, end="-")

