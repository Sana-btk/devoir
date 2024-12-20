
nombres = [1, 2, 3, 4, 5]

def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    index_input = input("Entrer un  index (-1 pour quiter): ")
    
    if index_input == "-1":
        break
    
    if not is_valid_integer(index_input):
        print("index invalide. Veuillez entrer un entier.")
        continue

    index = int(index_input)

    if index < 0 or index >= len(nombres):
        print("Indice hors de 'range'. Veuillez entrer un indice valide.")
        continue

    new_value = input("entrer un nouvelle valeur : ")

    if not is_valid_integer(new_value):
        print("Valeur invalide. Veuillez entrer un entier.")
        continue

    new_value = int(new_value)

    nombres[index] = new_value

    print(nombres)
