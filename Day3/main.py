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

print("Welcome to the roller coaster ride.")

height = int(input("What is your height?"))

if height >= 120:
    print("Yes you can ride.")
    age = int(input("How old are you? "))
    if age < 12:
        print("Please pay $5")
    elif age >= 12 or age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("No you are NOT tall enough.")
