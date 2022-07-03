# Highest score
# Calculate the highest student score from the user inputted list

elements = int(input('Please enter number of elements in the list: '))
scores = []

for i in range(elements):
    el = int(input('Enter element {}: '.format(i+1)))
    scores.append(el)

print(scores)

maximum = scores[0]
for score in range(len(scores)):
    if scores[score] > maximum:
        maximum = scores[score]

print(maximum)
# Visit: litcode.net and @thelitcode
