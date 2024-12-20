
mot = input("mot: ")

frame_width = 30

spaces = (frame_width - len(mot)) // 2

print(" " * spaces + mot + " " * (frame_width - len(mot) - spaces) + "*")
