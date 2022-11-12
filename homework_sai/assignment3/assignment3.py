def ex1(hours, wage):
    # Many companies pay time-and-a-half for any hours worked above 40 in a given week.
    # Complete this function whose inputs are hours worked (hours) and the hourly rate (wage) to
    # calculate the total wages for the week.
    #
    # BEGIN SOLUTION
    if hours > 40:
        return (hours-40)*(wage*1.5)+(40*wage)
    else:
        return hours*wage
    # END SOLUTION


def ex2(score):
    # A certain CS professor gives five-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F.
    # Complete this function which accepts a quiz score as an input and uses a decision structure to calculate the corresponding
    # grade.
    # BEGIN SOLUTION
    if score <=1:
        return 'F'
    elif score == 2:
        return 'D'
    elif score == 3:
        return 'C'
    elif score == 4:
        return 'B'
    else:
        return 'A'
    # END SOLUTION


def ex3(score):
    # A certain CS professor gives 100-point exams that are graded on the scale 90-100: A, 80-89: B, 70-79: C,
    # 69-69: D, < 60: F. Complete this function which accepts an exam score as input and uses a decision structure
    # to calculate the corresponding grade.
    # BEGIN SOLUTION
    if score >=90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'
    # END SOLUTION


def ex4(credits):
    # A certain college classifies students according to credits earned. A student with less than 7 credits is a Freshman.
    # At least 7 credits are required to be a Sophomore, 16 to be a Junior and 26 to be classified as Senior.
    # Complete this function which calculates the class standing from the number of credits earned.
    # BEGIN SOLUTION
    if credits < 7:
        return 'Freshman'
    elif credits >=26:
        return 'Senior'
    elif credits >=16:
        return 'Junior'
    else:
        return 'Sophomore'
    # END SOLUTION


def ex5(limit, speed):
    # The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a
    # penalty of $200 for any speed over 90 mph. Complete this function which accepts a speed limit and a clocked
    # speed and either return the string `Legal` or the amount of fine, if the speed is illegal.
    # BEGIN SOLUTION
    if speed < limit:
        return 'Legal'
    else:
        extra_speed = speed - limit
        fine = (extra_speed * 5)+50
        if speed > 90:
            fine+=200
            return fine
        return fine
    # END SOLUTION


def ex6(input_string):
    # Complete this function to determine if the input_string is a palindrome. Return True or False
    # Use square brackets to reverse the input_string! Make sure to lower the input string before testing!
    # BEGIN SOLUTION
    input_string=input_string.lower()
    palindrome=input_string[::-1]
    if input_string==palindrome:
        return True
    else:
        return False
    # END SOLUTION


def ex7(month, day):

    # The year is divided into four season: spring, summer, fall (or autumn) and winter.
    # While the exact dates that the seasons change vary a little bit from year to
    # year because of the way that the calender is constructed, we will use the following
    # dates for this exercise:

    # Season  -- First Day
    # Spring  -- March 20
    # Summer  -- June 21
    # Fall  -- September 22
    # Winter    -- December 21

    # Complete this function which takes in as inputs a month and day. It should
    # output the season.
    # input 1: month -- str
    # input 2: day -- int

    # output: month -- str (Spring, Summer, Fall, Winter)

    # BEGIN SOLUTION
    # month_dict = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
    if (month=='March' and day >=20) or month in ['April','May'] or (month =='June' and day<21):
        return 'Spring'
    elif (month=='June' and day >=21) or month in ['July','August'] or (month =='September' and day<22):
        return 'Summer'
    elif (month=='September' and day >=22) or month in ['October','November'] or (month =='December' and day<21):
        return 'Fall'
    else:
        return 'Winter'
    # END SOLUTION


def ex8(year):
    # Complete this function to check if year is a leap year
    # Input: year
    # Output: True or False (Boolean)

    # BEGIN SOLUTION
    year=str(year)
    return int(year[:2])%4==0 and int(year[2:])%4==0
    # END SOLUTION


def ex9(month, day, year):
    # Complete this function to check if a data is valid, given month, day, and year.
    # For example, 5/24/1962 is valid, but 9/31/2000 is not
    # Inputs: month, day, year
    # Output: True or False (Boolean)
    # IMPORTANT: Use the function ex8() to determine if year is leap year

    # BEGIN SOLUTION
    if ex8(year) == True:
        if month==2 and day>=29:
            return True
        if month<=7:
            if month%2!=0 and day<=30:
                return True
            elif month%2==0 and day<=31:
                return True
        else:
            if month%2!=0 and day<=30:
                return True
            elif month%2==0 and day<=31:
                return False
            else:
                return False    
    else:
        if month==2 and day>=28:
            return False
        if month<=7:
            if month%2!=0 and day<=30:
                return True
            elif month%2==0 and day<=31:
                return True
        else:
            if month%2!=0 and day<=30:
                return True
            elif month%2==0 and day<=31:
                return True
    # pass
    # END SOLUTION


def ex10(month, day, year):
    # Complete this function to calculate the day_number given month, day, and year.
    # Information: The days of the year are often numbered from 1 through 365 (or 366).
    # This number can be computed in three steps using int arithmetic:
    # (a) - day_num = 31 * (month - 1) + day
    # (b) - if the month is after February subtract (4*(month)+23)//10
    # (c) - if it's a leap year and after February 29, add 1
    # Hint: First verify the input date is valid, return False if it is not valid; use is_date_valid
    # IMPORTANT: use the functions you wrote previous, namely, ex8 and ex9.
    # Inputs: month, day, year
    # Output: the day number or False (boolean) if the date is invalid.

    # BEGIN SOLUTION

    # day_num = 31 * (month - 1) + day

    # if month==8:
    #     num_days=31
    # elif month%2!=0:
    #     num_days=31
    # else:
    #     num_days=30
    if ex9(month, day, year)==True:
        if ex8(year)== True:
            if month <= 2:
                day_num = 31 * (month - 1) + day
            else:
                day_num = ((31 * (month - 1) + day) - (4*(month)+23)//10) +1
            return day_num
        else:
            if month <= 2:
                day_num = 31 * (month - 1) + day
            else:
                day_num = ((31 * (month - 1) + day) - (4*(month)+23)//10)
            return day_num
    else:
        return False

    # END SOLUTION


def ex11(plate):

    # In a particular jurisdiction, older license plates consist of three uppercase
    # letters followed by three digits. When all of the license plates following
    # that pattern had been used, the format was changed to four digits followed by
    # three uppercase letters.

    # Complete this function whose only input is a license plate and its output
    # is: 1) Older/Valid 2) Newer/Valid 3) Invalid
    # input: plate (str)
    # output: 'Older/Valid' or 'Newer/Valid' or 'Invalid'
    # HINT: Use the comparator operators (>=, <=)!

    # BEGIN SOLUTION
    if len(plate)==6:
        if plate[:3].upper()!=plate[:3]:
            return 'Invalid'
        else:
            return 'Older/Valid'
       
    else:
        if plate[4:].upper()!=plate[4:]:
            return 'Invalid'
        else:
            return 'Newer/Valid'
        

    # END SOLUTION


def ex12(date):
    # A magic date is a date where the day multiplied by the month is equal
    # to the two digit year. For example, June 10, 1960 is a magic date because
    # June is the sixth month, and 6 times 10 is 60, which is equal to the two
    # digit year. Complete this function to determine whether or not a date is
    # a magic date.

    # input: date (str -- month/day/year) -- e.g., 06/01/2022 -- will have leading zero before month and day
    # output: True or False (bool)
    # Hint: use string indexing to extract the month, day, and year from the date string

    # BEGIN SOLUTION
    date=date.split('/')
    len_date=len(date)
    for i in range(len_date):
        date[i]=int(date[i])
    # print(date)
    if date[0]*date[1] == date[2]%100:
        return True
    else:
        return False
    # END SOLUTION
