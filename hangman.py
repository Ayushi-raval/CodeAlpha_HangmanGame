import random

f = open("words.txt", "r")
words = []                                  # a list of (category, word) pairs
for data in f:                              
    data = data.strip()
    if data.startswith("#") or ":" not in data:     # skip comment/empty lines
        continue
    category_name, word_part = data.split(":", 1)   # "Animals: tiger zebra" -> "Animals", " tiger zebra"
    for w in word_part.split():
        words.append((category_name.strip(), w))
f.close()

category, word = random.choice(words)       #  picks the category and the word together
word = word.upper()

total_chances = 6
guessed_word = "-"*len(word)

while total_chances != 0:
    print("Category:", category)            # shows the category hint
    print(guessed_word)
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
                #print(guessed_word)
        if guessed_word == word:
            print("Congratulations you won!!!")     # fixed spelling
            break

    else:
        total_chances -= 1
        print("Incorrect guess")
        print("The remaining chances are: ", total_chances)

else:
    print("Game over")
    print("You Lose")
    print("All the chances are exhausted") 

print("The correct word is " + word)
