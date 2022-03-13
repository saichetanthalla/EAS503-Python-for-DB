def ex1(name):
    # Complete this function to use the `name` input parameter/argument to create the following string and return it:
    # Hello, <name>, nice to meet you!
    # Example: name = Brian
    # Output: "Hello, Brian, nice to meet you!"
    # You must use f-string!!!
    return "Hello," +" " + f'{name},' +" "+  "nice to meet you!"
    ### BEGIN SOLUTION
    ### END SOLUTION



def ex2(x, y, z):
    # Complete this function to use the inputs x, y, and z to return the quoted string. 
    # You must use f-string to create each line, but you can use the + operator to join each line. 
    """
    The value of x is: <x>.
    The value of y is: <y>.
    The value of z is: <z>.

    """
    
    
    ### BEGIN SOLUTION
    return f"""The value of x is: {x}.
The value of y is: {y}.
The value of z is: {z}."""
     
    ### END SOLUTION


def ex3(length, width):
    # Complete this function to use the inputs length and width to 
    # calculate the area of a rectangle and return the following string:
    # "The area of a rectangle with length <length> and width <width> is <area>."
    # Make sure to round the area to two decimal places. 
    area=round(length * width,2)
    ### BEGIN SOLUTION
    return f"""The area of a rectangle with length {length} and width {width} is {area}."""
    ### END SOLUTION



def ex4(radius):
    # Complete this function to return the surface area of a sphere given a radius. 
    # Use the input `radius` as the radius
    # round the surface area to two decimals 
    # Use the PI from the math module
    
    import math
    PI = math.pi
    
    ### BEGIN SOLUTION
    area= 4 * PI* radius**2
    return round(area,2)
    ### END SOLUTION


def ex5(radius):
    # Complete this function to return the volume of a sphere given a radius. 
    # Use the input `radius` as the radius
    # round the surface area to two decimals 
    # Use the PI from the math module
    
    import math
    PI = math.pi
    
    ### BEGIN SOLUTION
    area= (4/3) * PI* radius**3
    return round(area,2)
    ### END SOLUTION


def ex6(weight, height):
    # The body mass index (BMI) is calculated as a peron's weight (in pounds) times 720, divided by the square
    # of the person's height (in inches). A BMI in the range 19-25, inclusive, is considered healthy. 
    # Complete this function to calculate and return a person's BMI 
    # Round the BMI to two decimals places
    
    ### BEGIN SOLUTION

    bmi = weight * 720 / (height ** 2)
    return round(bmi,2)

    ## END SOLUTION
    


def ex7(no_one_liter_bottles, no_more_than_one_liter_bottles):
    # When you buy soda bottles, you deposit a small amount to encourage recycling. 
    # For one liter bottle the deposit is $0.10.
    # For a bottle larger than one liter, the deposit is $0.25.
    # Complete this function to print a refund message like follows:
    # The refund amount is $<amount>.
    # Round the refund to two decimal places using f-string format specifier
    
    ### BEGIN SOLUTION
   
    ans= 0.10* no_one_liter_bottles + 0.25* no_more_than_one_liter_bottles
    return  f"""The refund amount is ${ans:.2f}."""
    ### END SOLUTION
    

def ex8(a, b):
    # Complete this function to return the following string given two numbers a and b
    """
    The sum of <a> and <b> is <result>.
    The difference when <b> is subtracted from <a> is <result>.
    The product of <a> and <b> is <result>.
    The quotient when <a> is divided by <b> is <result>.
    The remainder when <a> is divided by <b> is <result>. 
    The result of <a>^<b> is <result>. 
    """

    # Return just one string that has multiple lines. use f-string and + to concatenate lines

    ### BEGIN SOLUTION
    return f"""The sum of {a} and {b} is {a+b}.
The difference when {b} is subtracted from {a} is {a-b}.
The product of {a} and {b} is {a*b}.
The quotient when {a} is divided by {b} is {a//b}.
The remainder when {a} is divided by {b} is {a%b}.
The result of {a}^{b} is {a**b}."""



    ### END SOLUTION


def ex9(P, r, t):
    # The formula for simple interest is A = P(1+rt), where P is
    # the principle amount, r is the annual rate of interest,
    # t is the number of years the amount is invested, and A
    # is the amount at the end of the investment. 
    # Complete this function to return the following string:
    # After <t> years at <r>%, the investment will be worth $<A>.
    # Round the amount to two decimal places using f-string
    # Hint: rate is a percentage!
    
    ### BEGIN SOLUTION
    A = P*(1+(r*t/100))
    return f"""After {t} years at {r}%, the investment will be worth ${A:.2f}."""



    ### END SOLUTION


def ex10(P, r, t, n):
    # The formula for compound interest is 
    # A = P(1 + r/n)^nt
    # where:
    # P is the principle amount.
    # r is the annual rate of interest.
    # t is the number of years the amount is invested. 
    # n is the number of times the interest is compounded per year.
    # A is the amount at the end of the investment. 
    # Complete this function to return the following string:
    # $<P> invested at <r>% for <t> years compounded <n> times per year is $<A>.
    # round to two decimal places using f-string formatting

    
    ### BEGIN SOLUTION
    
    A = P*((1+r/(100*n))**(n*t))


    return f"""${P} invested at {r}% for {t} years compounded {n} times per year is ${A:.2f}."""
    ### END SOLUTION
    

def ex11(input_string):
    """
    This function takes in one input string. Complete this function to return
    the input string and the number of characters in the input string.
    Sample Input: Amherst
    Expected return string: The input string 'Amherst' has 7 characters. 
    - Use f-string
    """
 
    ### BEGIN SOLUTION

    return f"""The input string '{input_string}' has {len(input_string)} characters."""
    ### END SOLUTION


def ex12(noun, verb, adjective, adverb):
    """
    This function takes in four input strings. Complete this function to return
    a sentence using the four input strings
    Input Strings: noun, verb, adjective, adverb
    Expected print Statement: Do you <verb> your <adjective> <noun> <adverb>? That's hilarious!
    - Use f-string
    """
    
    ### BEGIN SOLUTION

    return f"""Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"""

    ### END SOLUTION   


def ex13(current_age, age_at_retirement, current_year):
    """
    This function takes in three numbers as input arguments: current_age, age_at_retirement, and current_year. 
    Complete this function to return the expected output string. 
      
    If current_age = 36, age_at_retirement = 72, and current_year = 2021
    
    Expected output:
    Your current age is: 36.
    You would like to retire at: 72.
    You have 36 years left until you can retire.
    It's 2021, so you can retire in 2057.
    
    - Use f-string
    """
    
    ### BEGIN SOLUTION

    return f"""Your current age is: {current_age}.
You would like to retire at: {age_at_retirement}.
You have {age_at_retirement-current_age} years left until you can retire.
It's {current_year}, so you can retire in {current_year + (age_at_retirement - current_age)}."""
     
   
    ### END SOLUTION


def ex14(length, width):
    """
    This function takes in the length and width in feet. 
    Complete this function to return the expected output string. 
    Use formula -- m^2 = f^2 * 0.09290304 to convert feet^2 to meter^2
    
    If length = 15 and width = 20
    
    Expected output:
    The length of the room in feet is 15.
    The width of the room in feet is 20.
    The dimension of the room is 15 by 20 feet.
    The area is
    300 square feet
    27.87 square meters

    - Use f-string
    """
    form= length*width*0.09290304
    ### BEGIN SOLUTION
   
    return f"""The length of the room in feet is {length}.
The width of the room in feet is {width}.
The dimension of the room is {length} by {width} feet.
The area is
{length*width} square feet
{form:.2f} square meters"""



    ### END SOLUTION


def ex15(number_of_people, number_of_pizzas):
    """
    This function takes in the number of people and the number of pizzas. Assume each pizza has 8 slices. 
    
    Complete this function to return the expected output string. 

    If number_of_people = 8 and number_of_pizzas = 2
    
    Expected output:
    There are 8 with 2 pizzas.
    Each person gets 2 pieces of pizza.
    There are 0 leftover pieces.

    - Use f-string
    """
    
    
    ### BEGIN SOLUTION

    return f"""There are {number_of_people} with {number_of_pizzas} pizzas.
Each person gets 2 pieces of pizza.
There are {(number_of_pizzas*8)%number_of_people} leftover pieces."""


    ### END SOLUTION


def ex16(length, width):
    """
    This function takes in the length and width in feet of a ceiling. You need to calculate the number
    of gallons needed to paint the ceiling. Assuming one gallon can paint 350 square feet. 
    
    Complete this function to return the expected output string. 

    If length = 12 and width = 30
    
    Expected output:
    You will need to purchase 2 gallons of paint to cover 360 square feet.

    - Use f-string
    - HINT: You need to use the math.ceil function to round up
    """
    
    import math
    ### BEGIN SOLUTION
    return f"""You will need to purchase {math.ceil((length*width)/350)} gallons of paint to cover {length*width} square feet."""
    
    ### END SOLUTION


def ex17(value):
    """
    You must use f-string formatting to get the output string: "The value is: 3.1416." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. Do not use the round
    function. Rather, use f-string for rounding. Make sure to return the output string!
    """

    ### BEGIN SOLUTION  
    return f"""The value is: {value:.4f}."""
    ### END SOLUTION


def ex18(value):
    """
    You must use f-string formatting to get the following string output: "The value is:     3.1416." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. Do not just put
    spaces inside the f-string. Use f-string format specifiers to adjust justification and width. 
    """

    ### BEGIN SOLUTION  

    return f"""The value is:{value:>11.4f}."""

    ### END SOLUTION


def ex19(value):
    """
    You must use f-string formatting to get the following string output: "The value is: 3.141590--.". This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output. 
    """

    ### BEGIN SOLUTION  
    return f"""The value is: {value:.6f}--."""

    ### END SOLUTION


def ex20(value):
    """
    You must use f-string formatting to get the followint output string: "The value is: --3.141590--." This is reverse engineering problem. 
    Start at the output and figure out how to use f-string format specifiers to get the desired output.   
    """
    ### BEGIN SOLUTION  
    return f"""The value is: --{value:.6f}--."""
    ### END SOLUTION