import random

class NumberGuessingGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

    def play(self):
        print("Welcome to the Number Guessing Game!")
        print("Guess a number between 1 and 100.")

        while True:
            guess = int(input("Your guess: "))
            self.attempts += 1

            if guess < self.number_to_guess:
                print("Too low! Try again.")
            elif guess > self.number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {self.number_to_guess} in {self.attempts} attempts.")
                break

# Start the game
game = NumberGuessingGame()
game.play()
