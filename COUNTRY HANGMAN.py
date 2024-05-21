import random

Hard_countries= ['Colombia','Barbados','Eritrea','Portugal','Sweden','Tajikistan','Cyprus']
Medium_countries = ['Philippines','Nigeria','Mauritius','Zimbabwe','Ukraine','Romania','Serbia']
Easy_countries = ['Argentina','Maldives','Poland','Egypt','Greece','Hawaii','Vietnam']


Name_Of_Player = input("enter your name : ")
print(f"Welcome {Name_Of_Player} to Hangman Game! Let's play with Countries.")

Choose_level = input("Choose the level for game - EASY , MEDIUM , HARD : ")
Choose_level = Choose_level.upper()
if(Choose_level == "EASY" ):
    
    Word = random.choice(Easy_countries)
    word_length = len(Word)
    display = ['_'] * word_length
    guessed_letters = []
    remaining_lives = 7
    print(f"The country has {word_length} letters.")

elif(Choose_level == "MEDIUM" ):
    Word = random.choice(Medium_countries)
    word_length = len(Word)
    display = ['_'] * word_length
    guessed_letters = []
    remaining_lives = 6
    print(f"The country has {word_length} letters.")

else:
    Word = random.choice(Hard_countries)
    word_length = len(Word)
    display = ['_'] * word_length
    guessed_letters = []
    remaining_lives = 5
    print(f"The country has {word_length} letters.")


while True:
    print(f"\nLives remaining: {remaining_lives}")
    print(' '.join(display))

    if '_' not in display:
        print(f"Congratulations {Name_Of_Player}! You guessed the Country '{Word}'.")
        break

    if remaining_lives == 0:
        print(f"Game Over! The country was '{Word}'.")
        break

    guess = input("Guess a letter: ").upper()

    if len(guess) != 1 :
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in Word.upper():
        
        indices = [i for i, letter in enumerate(Word.upper()) if letter == guess]
        for index in indices:
            display[index] = Word[index]
    else:
        remaining_lives -= 1
        print(f"'{guess}' is not in the Country.")
