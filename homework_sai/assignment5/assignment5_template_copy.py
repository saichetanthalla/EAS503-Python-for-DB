def ex1(lst):
    # Complete this function to use list comprehension to return all values from `lst`
    # that are a multiple of 3 or 4.
    # input: `lst` of numbers
    # output: a list of numbers
    
    # BEGIN SOLUTION
    pass
    # END SOLUTION



def ex2(lst):
    # Complete this function to use list comprehension to multiple all numbers
    # in the list by 3 if it is even or 5 if its odd
    # input: `lst` of numbers
    # output: a list of numbers
    
    # BEGIN SOLUTION
    pass
    # END SOLUTION

def ex3(filename):
    # Complete this function to read grades from `filename` and find the minimum
    # student test averages. File has student_name, test1_score, test2_score,
    # test3_score, test4_score, test5_score. This function must use a lambda
    # function and use the min() function to find the student with the minimum
    # test average. The input to the min function should be
    # a list of lines. Ex. ['student1,33,34,35,36,45', 'student2,33,34,35,36,75']
    # input filename
    # output: (lambda_func, line_with_min_student) -- example (lambda_func, 'student1,33,34,35,36,45')

    # BEGIN SOLUTION
    pass
    # END SOLUTION




def ex4(filename):
    # Complete this function to read grades from `filename` and map the test average to letter
    # grades using map and lambda. File has student_name, test1_score, test2_score,
    # test3_score, test4_score, test5_score. This function must use a lambda
    # function and map() function.
    # The input to the map function should be
    # a list of lines. Ex. ['student1,73,74,75,76,75', ...]. Output is a list of strings in the format
    # studentname: Letter Grade -- 'student1: C'
    # input filename
    # output: (lambda_func, list_of_studentname_and_lettergrade) -- example (lambda_func, ['student1: C', ...])

    # Use this average to do the grade mapping. Round the average grade.
    # D = 65<=average<70
    # C = 70<=average<80
    # B = 80<=average<90
    # A = 90<=average
    # Define a function that takes in a number grade and returns the letter grade and use
    # it inside the lambda function. 
    ## HINT: create a function 

    # BEGIN SOLUTION
    pass
    # END SOLUTION



def ex5(filename):
    # Complete this function to sort a list of dictionary by 'test3'
    # return the lambda function and the sorted list of dictionaries
    # Use the following code to read JSON file

    import json
    with open(filename) as infile:
        grades = json.load(infile)

    # BEGIN SOLUTION
    pass
    # END SOLUTION

def ex6(input_dict, test_value):
    # Complete this function to find all the keys in a dictionary that map to the input value. 
    # input1: input_dict (dict)
    # input2: test_value
    # output: list of keys

    # BEGIN SOLUTION
    pass
    # END SOLUTION


def ex7(filename):
    """
    In this problem you will read data from a file and perform a simple mathematical operation on each data point. 
    Each line is supposed to contain a floating point number.
    But what you will observe is that some lines might have erroneous entries. 
    You need to ignore those lines (Hint: Use Exception handling).

    The idea is to implement a function which reads in a file and computes the median 
    of the numbers and returns the output. You may use the inbuilt function sort when computing the median.

    DO NOT USE ANY INBUILT OR OTHER FUNCTION TO DIRECTLY COMPUTE MEDIAN
    """
    ### BEGIN SOLUTION
    pass
    ### END SOLUTION

def simulateProblem():
    """
    See instructions in exercise_8_instructions.html file
    """
    ### BEGIN SOLUTION
    pass
    ### END SOLUTION


def ex8():
    """
    The function calls the simulateProblem() 10000 times to figure out 
    the empirical (observed) probability of gaining more money when switch 
    and gaining more money when stick to the original choice.
    Return the probability of win due to stick and win due to switch
    """
    ### BEGIN SOLUTION
    pass
    ### END SOLUTION


def ex9(title, header, data, sort_header_name, filename):
    # This problem is EASY!!!!!
    # Open up ex9_*_solution.txt and look at the output based on the input parameters, which
    # can be found in the test_assignment5.py file
    # Function inputs: 
    # title -- title of the table -- a string
    # header -- header of the table  -- a tuple
    # data -- rows of data, which is a tuple of tuples
    # sort_header_name -- name of the header to sort the data by
    # filename -- name of file to write the table to
    # Your job is to create the table in the file and write it to `filename`
    # Note that you need to dynamically figure out the width of each column based on 
    # maximum possible length based on the header and data. This is what makes this problem hard. 
    # Once you have determined the maximum length of each column, make sure to pad it with 1 space
    # to the right and left. Center align all the values. 
    # OUTPUT: you are writing the table to a file
    # ******NOTE: USE sort_header_name to sort the data using sorted and lambda. Sorting might be incorrect, 
    # but that is fine. We will explore this issue in class. I just want you have the code in place. 
    # NOTE: sort in descending order

    ### BEGIN SOLUTION
    pass
    ### END SOLUTION