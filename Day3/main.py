# print("Welcome to the roller coaster ride.")

# height = int(input("What is your height?"))

# if height >= 120:
#     print("Yes you can ride.")
# else:
#     print("No you are NOT tall enough.")


############## ODD or EVEN #####################


# print("Welcome to Odd or Even Checker")

# number = int(input("What number would you like to check? "))

# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an Odd number")


################3 Nested If Condition ################

# print("Welcome to the roller coaster ride.")

# height = int(input("What is your height?"))

# if height >= 120:
#     print("Yes you can ride.")
#     age = int(input("How old are you? "))
#     if age < 12:
#         print("Please pay $5")
#     elif age >= 12 or age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("No you are NOT tall enough.")


############# BMI CALCULATOR #######################

# print("BMI Calculator")

# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# bmi = round(weight / (height * height))

# if bmi < 18.5:
#     print(f"BMI:{bmi} Underweight")
# elif bmi >= 18.5 or bmi <= 25:
#     print(f"BMI:{bmi} Normal Weight")
# elif bmi > 25 or bmi <= 30:
#     print(f"BMI:{bmi} Slightly overweight")
# elif bmi > 30 or bmi <= 35:
#     print(f"BMI: {bmi} Obese")
# else:
#     print(f"BMI:{bmi} Clinically Obese")


################# LEAP YEAR ########################

# 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
#     print("Leap Year!!!")
# else:
#     print("NOT Leap Year!")


# #########MULTIPLE IF's FINAL RIDE TICKETS#########

# print("Welcome to the roller coaster ride.")

# height = int(input("What is your height? "))
# price = 0

# if height >= 120:
#     print("Yes you can ride.")
#     age = int(input("How old are you? "))
#     if age < 12:
#         price = 5
#         print("Child $5")
#     elif age >= 12 or age <= 18:
#         price = 7
#         print("youth tickets $7")
#     else:
#         price = 12
#         print("Adult tickets $12")
#     pictures = input("Do you want pictures? Y/N")
#     if pictures == "Y":
#         print(f"Total price for ticket is ${price + 3} and $3 for the photo")
#     else:
#         print(f"Total price for ticket only is ${price}")
# else:
#     print("No you are NOT tall enough.")


# PIZZA ORDER ###################33333

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# size = size.upper()
# add_pepperoni = add_pepperoni.upper()
# extra_cheese = extra_cheese.upper()
# price = 0


# if size == "S":
#     price = 15
#     if add_pepperoni == "Y":
#         price += 2
# elif size == "M":
#     price = 20
#     if add_pepperoni == "Y":
#         price += 3
# elif size == "L":
#     price = 25
#     if add_pepperoni == "Y":
#         price += 3
# else:
#     print("Choose a valid size.")

# if extra_cheese == "Y":
#     price += 1

# print(f"Your final bill is ${price}")


################# Roller Coaster Mid-Life ################

# print("Welcome to the roller coaster ride.")

# height = int(input("What is your height? "))
# price = 0
# pictures = input("Do you want pictures? Y/N ")
# pictures = pictures.upper()

# if height >= 120:
#     print("Yes you can ride.")
#     age = int(input("How old are you? "))
#     if age < 12:
#         price = 5
#         print("Child $5")
#     elif age >= 12 and age <= 18:
#         price = 7
#         print("youth tickets $7")
#     elif age >= 45 and age <= 55:
#         price = 0
#     else:
#         price = 12
#         print("Adult tickets $12")

#     if pictures == "Y":
#         price += 3

#     print(f"Total price is ${price}.")


# else:
#     print("No you are NOT tall enough.")


###############33 LOVE SCORE #####################


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


combinedString = name1 + name2
lowString = combinedString.lower()

t = lowString.count("t")
r = lowString.count("r")
u = lowString.count("u")
e = lowString.count("e")

true = t + r + u + e

l = lowString.count("l")
o = lowString.count("o")
v = lowString.count("v")
e = lowString.count("e")

love = l + o + v + e

loveScore = int(str(true) + str(love))

if loveScore <= 10 or loveScore >= 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"You score is {loveScore} Lower than average.")
print(loveScore)
