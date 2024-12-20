import statistics

def print_statistics(lst):
    if lst:  
        mean = statistics.mean(lst)
        median = statistics.median(lst)
        print(f"Mean: {mean}")
        print(f"Median: {median}")
    else:
        print("No statistics available for an empty list.")

user_list = []

while True:
    try:
        number = int(input("Enter a number: "))
        
        if number == 0:
            break
        
        user_list.append(number)
        
        print(f"Current List: {user_list}")
        print(f"Sorted List (Ascending): {sorted(user_list)}")
        print(f"Sorted List (Descending): {sorted(user_list, reverse=True)}")
     
        print_statistics(user_list)
    
    except ValueError:
        
        print("Please enter a valid integer.")


with open("user_list.txt", "w") as file:
    file.write(str(user_list))
    print("\nList saved to 'user_list.txt'.")
