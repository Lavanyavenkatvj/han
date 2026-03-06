import random

# List of possible words
words = ["python", "developer", "hangman", "programming", "artificial", "intelligence"]

# Choose a random word
word = random.choice(words).lower()
guessed_letters = []
tries = 6  # Number of allowed incorrect guesses

# Display setup
print("Welcome to Hangman!")

# Game loop
while tries > 0:
    # Show current guessed state
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", " ".join(display_word))

    # Check for win
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Player input
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        tries -= 1
        print(f"Wrong guess. You have {tries} tries left.")

# Game over
if tries == 0:
    print("Game over! The word was:", word)
