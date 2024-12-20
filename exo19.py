
unique_words = set()
total_words = 0

while True:
    word = input("Enter a word: ").strip().lower() 
    
    total_words += 1  
    
    if word in unique_words:
     
        print(f"You typed in {len(unique_words)} unique words and {total_words} total words.")
        print("Unique words:", sorted(unique_words))  
        
       
        with open('unique_words.txt', 'w') as file:
            for word in sorted(unique_words):
                file.write(word + '\n')
        print("Unique words have been saved to unique_words.txt.")
        break
    else:
       
        unique_words.add(word)
