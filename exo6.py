
prix = float(input("Faites entrer le prix: "))

dinars = int(prix)  #partie entiere
centimes = int(round((prix - dinars) * 100))  #la partie decimale en entier

print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")
