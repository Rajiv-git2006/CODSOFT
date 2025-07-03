import random
import string

print("Welcome to the Password Generator\n")

while True:
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Please enter a positive number")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a number")

Letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation

all_characters = Letters + numbers + special_characters

password = "".join(random.choice(all_characters)for i in range(length))

print("\nThe Generated Password is :",password)

