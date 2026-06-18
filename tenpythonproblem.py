age=25


if age <13:
    print("chai")

elif age<20:
    print("teenager")

elif age<60:
    print("adult")

else:
    print("senior citizen")



#question2
age=22
day = "Wednesday"

price =12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2

print("ticket price is $" , price)


#question3
marks=89

if marks >=101:
    print("invalid marks")
    exit()


if marks >=90:
    print("A grade")

elif marks >=80:
    print("B grade")

elif marks >=70:
    print("C grade")

elif marks >=60:   
    print("D grade")

else:
    print("failed")


#Question4
#Determine if a fruit is ripe or not based on its color.

fruit_color = input("Enter the color of the fruit: ")
if fruit_color == "green":
    print("the fruit is not ripen")

elif fruit_color == "yellow":
    print("the fruit is ripen")

elif fruit_color == "red":
    print("the fruit is overripe")  

else:
    print("unknown fruit color")
