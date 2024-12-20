
mot = input("Entrer un mot: ")

est_palindrome = True

for i in range(len(mot) // 2):
    if mot[i] != mot[-(i + 1)]:
        est_palindrome = False
        break  

if est_palindrome:
    print("le mot est palindrome.")
else:
    print("le mot n'est pas palindrome.")
