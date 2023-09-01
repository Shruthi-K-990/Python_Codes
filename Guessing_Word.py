import random

name = input("Enter you're name")
print("Good Luck!", name)

words = ['mobile','laptop','keyboard','mouse','printer','scanner']
word= random.choice(words)
print(word)

print("Guess the characters")
gueses = ''

turn =10
while turn > 0:
    fail = 0
    for char in word:
        if char in gueses:
            print(char,end=" ")
        else:
            print("_")
            fail += 1

    if fail == 0:
        print("You win")
        print("The word is: ",word)
        break

    print()
    guess= input("Guess character")
    gueses += guess

    if guess not in word:
        print("You loose")
        turn-=1
        print("Wrong")
    print("You have", + turn, 'more guesses')

    if turn == 0:
        print("You Loose")

