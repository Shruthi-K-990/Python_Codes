import random
import math

lower_bound = int(input("Please enter lower bound value- "))
upper_bound = int(input("Please enter upper bound value- "))
count = 0

random_number = random.randint(lower_bound,upper_bound)
#print(random_number)
print("\n\tYou've only",round(math.log(upper_bound-lower_bound + 1,2)),
      "chances to guess the number!")

while count < math.log(upper_bound - lower_bound +1,2):
    count +=1

    guess = int(input("Guess the number"))

    if guess == random_number:
        print("Congratulations You have guessed it right in ",count,"count!")
        break
    if guess > random_number:
        print("You guessed high,Please try")
    if guess < random_number:
        print("you guessed low,Please try")

if count >= math.log(upper_bound-lower_bound +1,2):
    print("\n\tYou've reached maximum chances of ",count,"count,Better luck next time")



