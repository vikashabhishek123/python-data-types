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


#question5
#suggest an activity based on the weather conditions.

weather =input("Enter the weather condition (sunny, rainy, cloudy): ")

if weather =="sunny":
    print("It's a great day for a picnic!")

elif weather =="rainy":
    print("Don't forget your umbrella!")

elif weather =="cloudy":
    print("It might rain later, take a jacket just in case.")

else:
    print("Unknown weather condition. Please check the forecast.")



#Question 6
#Choose a mode of transportation based on the distance to be traveled.

distance =float(input("enter the distance to be traveled in km: "))

if distance <3:
    print("You can walk to your destination.")

elif distance <15:
    print("You can ride a bicycle to your destination.")

elif distance >15:
    print("You can take a bus or drive to your destination.")

else:
    print("Invalid distance entered.")


#Question7
#Customize a coffee order based on the customer's preferences.

order_size = input("Enter the size of your coffee (small, medium, large): ")
milk_preference = input("Do you want milk in your coffee? (yes/no): ")

if order_size == "small":
    if milk_preference == "yes":
        print("You ordered a small coffee with milk.")
    else:
        print("You ordered a small black coffee.")

elif order_size == "medium":
    if milk_preference == "yes":
        print("You ordered a medium coffee with milk.")
    else:
        print("You ordered a medium black coffee.")

elif order_size == "large":
    if milk_preference == "yes":
        print("You ordered a large coffee with milk.")
    else:
        print("You ordered a large black coffee.")

else:
    print("Invalid coffee size entered.")

    #Question8
    #Check password strength like weak, medium, strong based on certain criteria.

password = input("Enter your password: ")
if len(password) < 6:
    print("weak passwoed")

elif len(password) < 12:
    print("medium password")

elif len(password) >= 12:
    print("strong password")

else:
    print("invalid password")

#Question9
#Determine if a year is leap year or not.

year = int(input("Enter a year: "))
 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")

else:
    print(year, "is not a leap year.")

#Question10
#Puppy food ,e.g. Dog <2 years - puppy food, Dog >=2 years - adult dog food.
dog_age = float(input("Enter the age of the dog in years: "))

if dog_age < 2:
    print("Feed the dog puppy food.")

else:
    print("Feed the dog adult dog food.")