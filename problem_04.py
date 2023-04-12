def get_numbers_gt_5(myNumbers):
    my_numbers_gt_5 = []
    for num in myNumbers:
        if num > 5:
            my_numbers_gt_5.append(num)
    return my_numbers_gt_5


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_numbers_gt_5 = get_numbers_gt_5(my_numbers)

print("List of numbers:")
print(my_numbers)

print("List of numbers that are larger than 5:")
print(my_numbers_gt_5)
