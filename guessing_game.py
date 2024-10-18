import random 

number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter a guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"Your guess is correct! Attempts: {attempts}")
        break 
    
