import random

DIFFICULTIES = {

    "easy": 10,

    "medium": 5,

    "hard": 3,

}


def print_welcome():

    print("=" * 50)

    print("Welcome to the Number Guessing Game!")

    print("=" * 50)

    print("I'm thinking of a number between 1 and 100.")

    print("Choose a difficulty level to set how many chances you get:")

    print("  - easy   -> 10 chances")

    print("  - medium -> 5 chances")

    print("  - hard   -> 3 chances")

    print()


def choose_difficulty():

    while True:

        choice = input("Select difficulty (easy/medium/hard): ").strip().lower()

        if choice in DIFFICULTIES:

            return DIFFICULTIES[choice]

        print("Invalid choice. Please type 'easy', 'medium', or 'hard'.\n")


def get_guess(attempts_left):

    while True:

        raw = input(f"Enter your guess (1-100) [{attempts_left} chances left]: ").strip()

        if raw.isdigit() and 1 <= int(raw) <= 100:

            return int(raw)

        print("Please enter a whole number between 1 and 100.\n")


def play_game():

    print_welcome()

    chances = choose_difficulty()

    target = random.randint(1, 100)

    print(f"\nGreat! You have {chances} chances. Good luck!\n")

    for attempt in range(1, chances + 1):

        guess = get_guess(chances - attempt + 1)

        if guess == target:

            print(f"\n🎉 Congratulations! You guessed the number {target} correctly "

                  f"in {attempt} attempt{'s' if attempt > 1 else ''}!")

            return

        elif guess < target:

            print("Too low! The number is greater than your guess.\n")

        else:

            print("Too high! The number is less than your guess.\n")

    print(f"\n😔 Out of chances! The correct number was {target}. Better luck next time!")


def main():

    play_game()

    while True:

        again = input("\nPlay again? (y/n): ").strip().lower()

        if again == "y":

            print()

            play_game()

        elif again == "n":

            print("Thanks for playing! Goodbye.")

            break

        else:

            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":

    main()
 