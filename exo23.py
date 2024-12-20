
def get_positive_integer():
    while True:
        try:
            N = int(input("Veuillez entrer un integer positif: "))
            if N <= 0:
                print("Le nombre doit etre positif.")
            else:
                return N
        except ValueError:
            print("Entrer un integer valide.")

N = get_positive_integer()

for i in range(-N, N + 1):
    if i != 0:
        print(i)
