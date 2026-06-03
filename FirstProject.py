import random
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number (1-100): ")
    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("too low! try again.")
    elif guess > secret_number:
        print("too high! try again.")
    else:
       print(f"Correct! you got it in {attempts} tries.")
       break
