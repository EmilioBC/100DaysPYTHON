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


# ########################MULTIPLE IF's ########################3

print("Welcome to the roller coaster ride.")

height = int(input("What is your height? "))
price = 0

if height >= 120:
    print("Yes you can ride.")
    age = int(input("How old are you? "))
    if age < 12:
        price = 5
        print("Child $5")
    elif age >= 12 or age <= 18:
        price = 7
        print("youth tickets $7")
    else:
        price = 12
        print("Adult tickets $12")
    pictures = input("Do you want pictures? Y/N")
    if pictures == "Y":
        print(f"Total price for ticket is ${price + 3} and $3 for the photo")
    else:
        print(f"Total price for ticket only is ${price}")
else:
    print("No you are NOT tall enough.")
