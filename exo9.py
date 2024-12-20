
villes = []

#l'utilisateur fait entrer les noms des villes
while True:
    nomVille = input("Entrer le nom d'une ville ou 'stop' por arreter ").strip()
    
    if nomVille.lower() == 'stop':
        break
    
    #calculer population
    population = len(nomVille) * 1000000
    
    villes.append((nomVille, population))

#trier
villes.sort(key=lambda ville : ville[1], reverse=True)
#key : une fonction qui détermine la valeur utilisée pour le tri (Ici, on utilise une fonction anonyme appelée lambda)
#lambda : une fonction compacte et anonyme
#ville : élément de la liste villes
#ville[1] : accède à la deuxième valeur du tuple (la population) comme dans ("Paris", 5000000)

for ville , population in villes:
    print(f"ville: {ville}, Population: {population}")
