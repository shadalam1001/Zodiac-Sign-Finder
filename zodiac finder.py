                # Zodiac Finder
month = input("Enter your Birth month: ")
day = int(input("Enter month date: "))

# January
if month == "january":
    if day <= 19 and day > 0:
	    print("Your Zodiac sign is Capricorn")
    elif day >= 20 and day <= 31:
        print("Your Zodiac sign is Aquarius")
    else:
        print(f"Wrong date {day}")
# February
elif month == "february":
    if day <= 18 and day > 0:
	    print("Your Zodiac sign is Aquarius")
    elif day >= 19 and day <= 29:
        print("Your Zodiac sign is Pisces")
    else:
        print(f"Wrong date {day}")
# March
elif month == "march":
    if day <= 20 and day > 0:
	    print("Your Zodiac sign is Pisces")
    elif day >= 21 and day <= 31:
        print("Your Zodiac sign is Aries")
    else:
        print(f"Wrong date {day}")
# April
elif month == "april":
    if day <= 19 and day > 0:
	    print("Your Zodiac sign is Aries")
    elif day >= 20 and day <= 30:
        print(f"Your Zodiac sign is Taurus {day}")
    else:
        print("Wrong date")
# May
elif month == "may":
    if day <= 20 and day > 0:
	    print("Your Zodiac sign is Taurus")
    elif day >= 21 and day <= 31:
        print("Your Zodiac sign is Gemini")
    else:
        print(f"Wrong date {day}")
# June
elif month == "june":
    if day <= 20 and day > 0:
	    print("Your Zodiac sign is Gemini")
    elif day >= 21 and day <= 30:
        print("Your Zodiac sign is Cancer")
    else:
        print(f"Wrong date {day}")
# July
elif month == "july":
    if day <= 22 and day > 0:
	    print("Your Zodiac sign is Cancer")
    elif day >= 23 and day <= 31:
        print("Your Zodiac sign is Leo")
    else:
        print(f"Wrong date {day}")
# August
elif month == "august":
    if day <= 22 and day > 0:
	    print("Your Zodiac sign is Leo")
    elif day >= 23 and day <= 31:
        print("Your Zodiac sign is Virgo")
    else:
        print(f"Wrong date {day}")
# September
elif month == "september":
    if day <= 22 and day > 0:
	    print("Your Zodiac sign is Virgo")
    elif day >= 23 and day <= 30:
        print("Your Zodiac sign is Libra")
    else:
        print(f"Wrong date {day}")
# October
elif month == "October":
    if day <= 22 and day > 0:
	    print("Your Zodiac sign is Libra")
    elif day >= 23 and day <= 31:
        print("Your Zodiac sign is Scorpio")
    else:
        print(f"Wrong date {day}")
# November
elif month == "November":
    if day <= 21 and day > 0:
	    print("Your Zodiac sign is Scorpio")
    elif day >= 22 and day <= 30:
        print("Your Zodiac sign is Sagittarius")
    else:
        print(f"Wrong date {day}")
# December
elif month == "December":
    if day <= 21 and day > 0:
	    print("Your Zodiac sign is Sagittarius")
    elif day >= 22 and day <= 31:
        print("Your Zodiac sign is Capricorn")
    else:
        print(f"Wrong date {day}")
else:
    print(f"no month is named {month}")


