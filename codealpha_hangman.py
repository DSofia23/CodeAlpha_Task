import random

# Predefined list of words
words = ["apple", "banana", "grapes", "orange", "mango"]

# Randomly choose a word
word = random.choice(words)
word_letters = list(word)  # convert to list for easier checking
guessed = ["_"] * len(word)

# Game variables
attempts = 6
guessed_letters = []

print("🎯 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print(" ".join(guessed))

# Game loop
while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    # Check if letter already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word_letters:
        print("✅ Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)

    print(" ".join(guessed))

# End of game
if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Out of attempts! The word was:", word)
