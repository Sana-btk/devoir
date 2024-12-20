
people = int(input("nombre de personne ? "))
taxi_capacity = int(input("capacite d'un seul taxi ? "))

#calc le nbr de taxis
full_taxis = people // taxi_capacity
extra_taxi = 1 if people % taxi_capacity != 0 else 0

total_taxis = full_taxis + extra_taxi

print(f"nombre de taxis : {total_taxis}")
