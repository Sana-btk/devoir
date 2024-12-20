
name = input("Veuillez entrer votr nom: ")

if name == "VIP":
    print("Amusez vous gratuitement vous etes privilegie !")
else:
    #calculer le prix
    ticket_price = 15.50
    num_tickets = int(input("Combien de tiquet voulez vous acheter ? "))
    total_cost = ticket_price * num_tickets
    print(f"Total {total_cost}")
   
