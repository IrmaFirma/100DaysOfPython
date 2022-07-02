# Treasure Island 🏝
# Based on the user's choices guide them and 
# determine their fate and game results
# choices diagram can be found on the LitCode's latest post

# 🚀 SOLUTION:
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

directions = input('Would you like to go left or right? ')

if directions == 'left':
    left = input('Would you like to swim or wait? ')
    if left == 'wait':
        door = input('Which door; blue, red or yellow? ')
        if door == 'red':
            print('Burned by fire. Game Over!😔')
        elif door == 'blue':
            print('Eaten by beasts. Game Over!😔')
        elif door == 'yellow':
            print('You win! Congrats 🎉')
        else:
            print('Mission failed. Game Over!😔')
    else:
        print("You've been attacked! Game Over.😔")

if directions == 'right':
    print('You fell into a hole. Game Over!😔')
    
    
#Visit: litcode.net
