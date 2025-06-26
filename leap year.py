# Input a year from the user
year = int(input("Enter a year: "))

# Leap year logic:
# 1. If divisible by 4, go to step 2. Else, not a leap year.
# 2. If divisible by 100, go to step 3. Else, it's a leap year.
# 3. If divisible by 400, it's a leap year. Else, not a leap year.

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
