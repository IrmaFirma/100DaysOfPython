# Password Generator 💎
# By asking a user 3 simple questions
# Generate and display their password

import random

print('Welcome to Password Generator!')
l = int(input('How many letters do you want in your password? '))
s = int(input('How many symbols do you want in your password? '))
n = int(input('How many numbers do you want in your password? '))

# LISTS
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Generating random values from each list
user_password = []
for i in range(l+1):
    user_password.append(random.choice(letters))

for i in range(s+1):
    user_password.append(random.choice(symbols))

for i in range(n+1):
    user_password.append(random.choice(numbers))

# Shuffling the order of list elements
random.shuffle(user_password)

# Printing the result in one line
print('Your password is: ')
for i in user_password:
    print(i, end="")

print()
# Visit: litcode.net and @thelitcode
