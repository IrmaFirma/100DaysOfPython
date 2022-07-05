# Hangman game 🎮
# While following the steps commented create a computer version
# of the famous Hangman game

import random

# Stages that will be shown in the game after the user's guess
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========

''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



end_of_game = False
lives = 6

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
length = len(chosen_word)

# In this list there is the same number of _ as the letters in the chosen word
display = []
for i in range(length):
    display += '_'

# While the user has lives and hasn't won yet, prompt for their guess
while not end_of_game:
    guessed_letter = input('Guess the letter: ').lower()
    
    # Go through your chosen word and check 
    # if current letter of the chosen word equals guessed letter
    # replace the current _ in display with the chosen word letter
    for i in range(length):
        if chosen_word[i] == guessed_letter:
            display[i] = chosen_word[i]
    
    # Reduce lives if the letter doesn't exits
    # After lives hit 0 changed game status and message
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose!')

    # If all the _ are replaces with letters
    # Change the game status and message
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print user's current progress
    print(f"{' '.join(display)}")
    
    # print ASCII art of stages based on num of lives
    print(stages[lives])
    
    
# Visit: litcode.net and @thelitcode
