from google.generativeai import GenerativeModel
import random

model = GenerativeModel("gemini-pro")

print("Guessing Number Game")

number = random.randint(1, 50)

while True:
    guess = int(input("Guess a number: "))

    if guess == number:
        print("Correct! Well done!")
        break
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")
