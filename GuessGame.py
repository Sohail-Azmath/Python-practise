
import random
jackpot_num = random.randint(1,100)

guess_num = int(input("Enter a guess number:"))
count = 1
while guess_num != jackpot_num:
    count += 1
    if(guess_num < jackpot_num):
        print("Guess higher")
    else:
        print("Guess lower")
    guess_num = int(input("Enter a guess number:"))

print("Correct guess!! Congratulations")
print("No. of attempts:",count)