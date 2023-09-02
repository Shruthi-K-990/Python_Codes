import random
num= random.randrange(1000,9999)
print(num)
guess = int(input("guess digit number between 1000 to 9999 : "))
if num == guess:
    print("Hurray You've guess right number ",guess)

else:
    ctr=0
    while(guess != num):
        ctr +=1
        count = 0
        guess=str(guess)
        num=str(num)
        correct = ['X']*4
        for i in range(0,4):
            if guess[i] == num[i]:
                count+=1
                correct[i] = guess[i]
            else:
                continue
        if (count < 4) and (count != 0):
            print("Not quite the number. But you did get ",
              count, " digit(s) correct!")
            print("Also these numbers in your input were correct.")
            for k in correct:
                print(k, end=' ')

            print("\n")
            guess=int(input("Enter your next choice of number: "))

        elif count == 0:
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))


        if guess == num:

            ctr += 1
            print("You've become a Mastermind!")
            print("It took you only", ctr, "tries.")






