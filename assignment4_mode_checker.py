from google.generativeai import GenerativeModel

model = GenerativeModel("gemini-pro")

print("Mode Checker Game")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number ✅")
else:
    print("Odd Number ✅")
