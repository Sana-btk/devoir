
numbers = []
shoe_sizes = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

numbers.append(3)
numbers.append(5)

shoe_sizes = []
for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

combined_list = numbers + shoe_sizes

print("Liste des nombre:", numbers)
print("Liste des pointures:", shoe_sizes)
print("Liste generale :", combined_list)
