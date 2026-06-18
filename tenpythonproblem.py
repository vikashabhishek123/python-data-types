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

