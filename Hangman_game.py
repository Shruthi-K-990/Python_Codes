import random

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''
someWords=someWords.split()
word= random.choice(someWords)
print(word)
print("Hint it's a fruit")
guess=input("Guess the word:")
turn =10
while turn > 0:
    fail = 0
    for char in word:
        if char in guess:
            print(char,end=" ")
        else:
            print("_")
            fail += 1
    if fail == 0:
        print()
        print("You win")
        print("The word is: ",word)
        break

    g = input("Guess character")
    guess += g








