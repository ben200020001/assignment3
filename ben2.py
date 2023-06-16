#list of numbers
numbers = [1,-1,2,-3,3,-4,7,-6]

sum = 0

for num in numbers:
    if num < 0:
        continue
    else:
        sum += num

print("the sum of positive numbers:",sum)