#q1 write a function to calculate and return square of a number
def square(number):
    return number ** 2

    result = square(5)
    print(result)

#q2 write a function which takes two no. as a parameter and return the sum of two numbers

def two_number(number1,number2):
    return number1+number2

result = two_number(5,10)
print("the sum of two numbers is:", result)



#q3 write a function that multiply two numbers 

 def multiply(num1,num2):
    return num1*num2
result = multiply(5,10)
print("the multiplication of two numbers is:", result)



#q4 write a function that returns area and circumererce by taking radius as a parameter

def circle(radius):
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return area, circumference

result = circle(5)
print("the area of the circle is:", result[0])
print("the circumference of the circle is:", result[1])


#q5 write a a function that gives cube of a number

def cube(number):
    return number ** 3
result = cube(5)
print("the cube of the number is:", result)


#now doing the same thing using lambda function
cube = lambda x: x ** 3
result = cube(5)
print("the cube of the number using lambda function is:", result)