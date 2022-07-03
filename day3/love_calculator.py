# Love Calculator 🧡💛💚💙💜
# Calculations based on BuzzFeed's article
# Checking the score based on TRUE and LOVE

print('Welcome to Love Calculator!')
name1 = input('Please enter Partner 1 name: ').lower()
name2 = input('Please enter Partner 2 name: ').lower()

true_score = 0
love_score = 0

# checking TRUE for name1
if 't' in name1:
    true_score = true_score + 1
if 'r' in name1:
    true_score = true_score + 1
if 'u' in name1:
    true_score = true_score + 1
if 'e' in name1:
    true_score = true_score + 1

# checking TRUE for name2
if 't' in name2:
    true_score = true_score + 1
if 'r' in name2:
    true_score = true_score + 1
if 'u' in name2:
    true_score = true_score + 1
if 'e' in name2:
    true_score = true_score + 1


# checking LOVE for name1
if 'l' in name1:
    love_score = love_score + 1
if 'o' in name1:
    love_score = love_score + 1
if 'v' in name1:
    love_score = love_score + 1
if 'e' in name1:
    love_score = love_score + 1

# checking LOVE for name2
if 'l' in name2:
    love_score = love_score + 1
if 'o' in name2:
    love_score = love_score + 1
if 'v' in name2:
    love_score = love_score + 1
if 'e' in name2:
    love_score = love_score + 1

# forming a result
result = 0
if true_score != 0:
    result = (true_score*10)+love_score
else:
    result = love_score

# calculating the score
if result > 89:
    print('Your score is: {}%. You go together like coke with mentos.'.format(result))
elif result > 59 and result < 89:
    print('Your score is: {}%. You are able to work it out'.format(result))
elif result < 59:
    print('Your score is: {}%. Not a match.'.format(result))
    
    
# Visit: litcode.net and @thelitcode
