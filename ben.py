num = int(input("Enter a number: "))
total = 0

while num >= 0:
    if num < 0:
        break
    elif num >= 0:
        total = total + num
        num = int(input("Enter another number: "))
        continue
print("The sum of all positive numbers entered is:",total)
