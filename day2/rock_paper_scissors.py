# Rock, Paper, Scissors game ✂️
# Create a program that creates an interactive RPS game
# User enters their choice, computer displays theirs and the result is determined

import random

print('Welcome to Rock, Paper, Scissors!')
print('For ROCK type 0, PAPER type 1 and SCISSORS type 2')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choices = [rock, paper, scissors]

user_choice = int(input('Your choice: '))
print(choices[user_choice])

comp_choice = random.randint(0, 2)

print(choices[comp_choice])

if user_choice == comp_choice:
    print('It is a draw!')
elif user_choice == 0 and comp_choice == 1:
    print('Computer won! Sorry.')
elif user_choice == 0 and comp_choice == 2:
    print('You won. Congrats!')
elif user_choice == 1 and comp_choice == 2:
    print('Computer won. Sorry!')
elif comp_choice == 0 and user_choice == 1:
    print('You won. Congrats!')
elif comp_choice == 0 and user_choice == 2:
    print('Computer won. Sorry!')
elif comp_choice == 1 and user_choice == 2:
    print('You won. Congrats!')
    
    
    
# Visit: litcode.net and @thelitcode
