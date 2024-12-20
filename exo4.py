
age1 = int(input("Entrez l'age de la premiere personne: "))
age2 = int(input("Entrez l'age de la deuxieme personne: "))

if age1 > age2:
    print(f"Le plus grand: {age1}")
elif age2 > age1:
    print(f"Le plus grand: {age2}")
else:
    print("Le meme age")
