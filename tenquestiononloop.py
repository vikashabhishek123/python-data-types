#loops in python

#question 1 given a list of numbers, you have to find positive numbers in the list
numbers =[4, -3, 2, -1, 0, 5, -6]
positive_numbers_count=0
for num in numbers:
    if num >0:
        positive_numbers_count += 1

print("The count of positive numbers in the list is:", positive_numbers_count)


#Question 2
#sum of even numbers 

n=10
sum_even=0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1

print("The sum of even numbers from 1 to", n, "is:", sum_even)


#Question 3q    
#print the multiplication table of a given number
number =3

for i in range(1, 11):
    if i==5:
        continue
    result = number * i
    print(number, "x", i, "=", result)

#question 4
#reverse a string using loop 
