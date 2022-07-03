# Average height
# Calculate aveage height from the user inputted list

elements = int(input('Enter the number of heights in the list: '))
heights = []
height_sum = 0

for i in range(elements):
    ele = int(input('Element {}: '.format(i+1)))
    heights.append(ele)
    height_sum = height_sum + ele

print(round((height_sum/elements)))
# Visit: litcode.net and @thelitcode
