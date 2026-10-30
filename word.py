
import random
import string
from collections import Counter


# PART A: Number Guessing Game
def number_guessing_game():

    print("\n--- NUMBER GUESSING GAME ---")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                attempts -= 1
                continue

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                score = max(0, 100 - (attempts - 1) * 10)

                print("\nCongratulations! You guessed correctly.")
                print("Attempts:", attempts)
                print("Your score:", score)
                break

        except ValueError:
            print("Invalid input! Enter numbers only.")


# PART B: Word Counter
def word_counter():

    print("\n--- WORD COUNTER ---")

    filename = input("Enter text file name (example: sample.txt): ")

    try:
        with open(filename, "r") as file:
            text = file.read()

        # Convert text to lowercase
        text = text.lower()

        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))

        # Split text into words
        words = text.split()

        # Count word frequency
        frequency = Counter(words)

        print("\nTotal words:", len(words))
        print("Unique words:", len(frequency))

        print("\nWord Frequency:")

        for word, count in frequency.most_common():
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found! Please check the file name.")


# MAIN MENU
while True:

    print("\n==============================")
    print(" NUMBER GUESSING & WORD COUNTER")
    print("==============================")

    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number_guessing_game()

    elif choice == "2":
        word_counter()

    elif choice == "3":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please try again.")
