
montant = float(input("montant total: "))
num_articles = int(input("Nombre d'article: "))
jour = input("Jour de semaine: ").strip().capitalize()

discount = 0

if jour in ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi"]:
    discount += 10  # remise de 10% pour les jours de semaine
elif jour in ["Vendredi", "Samedi"]:
    discount += 20  # remise de 20% pour le weekend 

if num_articles > 5:
    discount += 5  # + 5% de remise

#prix apres remise
discounted_price = montant * (1 - discount / 100)

print(f"Prix total apres remise : {discounted_price:.1f} dinars")
