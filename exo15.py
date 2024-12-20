
user_input = input("Entrer un mot: ")

voy = ['a', 'e', 'o']

for vowel in voy:
    if vowel in user_input:
        print(f"{vowel} trouvee")
    else:
        print(f"{vowel} non trouvee")
