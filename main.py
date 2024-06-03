# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 28

year = None
month = None
day = None

# Check for leap year

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Check for acceptable days in month

def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 0

# check for integers and prompt user for input until valid integer recieved

def checkInput(prompt):
    while True:
        try:
            return int(input(prompt)) # attempts to convert the input to an integer
        except ValueError: # if input is not a valid integer, exception ValueError is raised
            print("Invalid input. Please enter a valid integer.") # prompt user to eneter a valid integer

# Get the year, then the month, then the day
# housekeeping()

month = checkInput("Enter a month (numeric MM): ")
day = checkInput("Enter a day (numeric DD): ")
year = checkInput("Enter a year (numeric YYYY): ")

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
else:
    MAX_DAY = days_in_month(month, year) # Get max days in month and year
    if day < MIN_DAY or day > MAX_DAY: # invalid day
        validDate = False

# Test to see if date is valid and output date and whether it is valid or not

# endOfJob()
if validDate == True:
    print(month,"/",day,"/",year, "is a valid date.")
else:
    print(month,"/",day,"/",year, "is an invalid date.")
