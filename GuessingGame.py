import random
jackpot_num = random.randint(1,10)
count = None
guess_num = int(input("Enter a jackpot number:"))
count = 1
while guess_num != jackpot_num:
    count += 1
    print("Try again")
    guess_num = int(input("Enter a jackpot number:"))
    if(guess_num == jackpot_num):
        break
    if(guess_num > 0 and guess_num < 10):
        print("Guess Lower")
    elif(guess_num > 10 and guess_num < 20):
        print("Guess higher")
    elif(guess_num > 20 and guess_num < 30):
        print("Guess higher")
    elif(guess_num > 30 and guess_num < 40):
        print("Guess higher")
    elif(guess_num > 40 and guess_num < 50):
        print("Guess higher")
    elif(guess_num > 50 and guess_num < 60):
        print("Guess lower")

print("Congratulations! You guessed the jackpot number")
print("No. of attempts:",count)