#lesson5
import random


secret_num=random.randint(1,10)
# print(secret_num)

guess=int(input("Guess a number between 1 - 10:"))


if secret_num == guess:
    print("Congrats you guessed it right.")
elif secret_num > guess:
     print("Too high.")
else: 
    print("Too low.")