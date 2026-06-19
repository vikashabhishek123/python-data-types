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
input_string = "Pythion"
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string

print("The reversed string is:", reversed_string)

#question5
#we have to write a program that find a non repeating character in a string
 input_string = "hello"

 for char in input_string:
        if input_string.count(char) == 1:
            print("The first non-repeating character is:", char)
            break



#question 6
#write a program to find the factorial of a number using while loop   

number=5
factorial=1

while number > 0:
    factorial = factorial * number
    number = number-1

    print("The factorial of the number is:", factorial)