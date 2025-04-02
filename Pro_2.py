import random
a = random.randint(1, 100)
n = -1
guess = 0

while n != a:
    guess += 1
    n = int(input("Guess the number: "))
    if n > a:
        print("Enter a lower number")
    elif n < a:
        print("Enter a higher number")

print(f"Exactly! You entered: {n}, and the system chose: {a} in {guess} attempts.")




