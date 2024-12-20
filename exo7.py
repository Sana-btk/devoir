
annee = int(input("Entrez l'annee : "))

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("Annee bissextile.")
else:
    print("Annee non bissextile.")
