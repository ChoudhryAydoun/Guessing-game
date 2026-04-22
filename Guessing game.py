import random

print("Select difficulty:")
print("1. Easy (1–50)")
print("2. Medium (1–100)")
print("3. Hard (1–200)")

difficulty = input("Choose: ")

if difficulty == "1":
    max_num = 50
elif difficulty == "2":
    max_num = 100
elif difficulty == "3":
    max_num = 200
else:
    print("Invalid choice, defaulting to Medium")
    max_num = 100

number = random.randint(1, max_num)
attempts = 0

print(f"\nGuess the number between 1 and {max_num}!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")