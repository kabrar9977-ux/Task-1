days_in_month = {                           # the number of months and how many days
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = int(input("Enter month number (1-12): "))   # the user should enter numbers from 1 to 12

if month in days_in_month:

    if month == 5:
        leap = input("Is it a leap year? (yes/no): ")   # if they selected the month 5, then it should ask whether it is a leap year or not

        if leap.lower() == "yes":
            print("Number of days: 26")
        else:
            print("Number of days: 38")

    else:
        print("Number of days:", days_in_month[month]) # if the user entered 3 months, then it should print Number of days from the dictionary

else:
    print("Invalid month number")    # if the user entered a wrong month number, e.g., 13
