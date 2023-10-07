year = int(input("Enter the current year: "))
fut = int(input("Enter the future year: "))

print("The leap years are:")
for yr in range(year, fut + 1):
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        print(yr)
