def LeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True
        
def daysMonth(year, month):
    if LeapYear(year):  # Correctly use the result of the LeapYear function
        days_in_month = {
            1: 31,  # January
            2: 29,  # February for leap year
            3: 31,  # March
            4: 30,  # April
            5: 31,  # May
            6: 30,  # June
            7: 31,  # July
            8: 31,  # August
            9: 30,  # September
            10: 31, # October
            11: 30, # November
            12: 31  # December
        } 
        return days_in_month[month]   # Correct bracket and removed print inside return

    else:
        days_in_month = {
            1: 31,  # January
            2: 28,  # February for non-leap year
            3: 31,  # March
            4: 30,  # April
            5: 31,  # May
            6: 30,  # June
            7: 31,  # July
            8: 31,  # August
            9: 30,  # September
            10: 31, # October
            11: 30, # November
            12: 31  # December
        }
        return days_in_month[month]   # Correct bracket for dictionary access

# Testing the function
print(daysMonth(2020, 2))  # Testing a leap year and February
