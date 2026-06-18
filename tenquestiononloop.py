#loops in python

#question 1 given a list of numbers, you have to find positive numbers in the list
numbers =[4, -3, 2, -1, 0, 5, -6]
positive_numbers_count=0
for num in numbers:
    if num >0:
        positive_numbers_count += 1

print("The count of positive numbers in the list is:", positive_numbers_count)

