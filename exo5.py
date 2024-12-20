
print("Runner 1:")
nom1 = input("Nom: ")
time1 = float(input("chrono (en secondes): "))

print("Runner 2:")
nom2 = input("Nom: ")
time2 = float(input("chrono (en secondes): "))

if time1 < time2:
    print(f"Le plus rapide est : {nom1}")
elif time2 < time1:
    print(f"Le plus rapide est : {nom2}")
else:
    print(f"{nom1} and {nom2} ont fait le meme chrono")
