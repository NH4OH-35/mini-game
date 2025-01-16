import random
def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it.")
    number_to_guess = random.randint(1, 100)
    attempts = 10
    while attempts > 0:
        try:
            guess = int(input(f"Enter your guess (Attempts left: {attempts}): "))
            if guess == number_to_guess:
                print("Congratulations! You guessed the number!")
                break
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            attempts -= 1
        except ValueError:
            print("Please enter a valid number.")
    if attempts == 0:
        print(f"Sorry, you're out of attempts. The number was {number_to_guess}.")
if __name__ == "__main__":
    guess_the_number()
#last edit 16/1/2025