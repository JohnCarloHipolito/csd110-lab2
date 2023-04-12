myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myNumbersGt5 = []

print("List of numbers:")
print(myNumbers)

for num in myNumbers:
    if num > 5:
        myNumbersGt5.append(num)

print("List of numbers that are larger than 5:")
print(myNumbersGt5)

