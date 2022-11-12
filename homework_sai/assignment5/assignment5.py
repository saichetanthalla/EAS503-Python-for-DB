def ex1(lst):
    # Complete this function to use list comprehension to return all values from `lst`
    # that are a multiple of 3 or 4.
    # input: `lst` of numbers
    # output: a list of numbers
    
    # BEGIN SOLUTION
    out=[items for items in lst if items%3==0 or items%4==0]
    return out
    # END SOLUTION



def ex2(lst):
    # Complete this function to use list comprehension to multiple all numbers
    # in the list by 3 if it is even or 5 if its odd
    # input: `lst` of numbers
    # output: a list of numbers
    
    # BEGIN SOLUTION
    # out=[items*3 for items in lst if items %2==0 else items*5]
    out=[elem*3 if elem%2==0 else elem*5 for elem in lst]
    return out
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
    # open filename as
    with open(filename) as file: 
        input_data=[]
        for line in file:
            line=line.strip()
            if line!="":
                input_data.append(line)
    lambda_function = lambda x: sum(list(map(int, x.split(",")[1:]))) / len(x.split(",")[1:])
    new_list = min(input_data, key=lambda_function)
    return (lambda_function, new_list)
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
    with open(filename) as file: 
        input_data=[]
        for line in file:
            line=line.strip()
            if line!="":
                input_data.append(line)
    
    def letter_grade(score): 
    # BEGIN SOLUTION
        if score >=90:
            return 'A'
        elif score >=80:
            return 'B'
        elif score >=70:
            return 'C'
        else:
            return 'D'
    lambda_function=lambda line:f"{line.split(',')[0]}: {letter_grade(round(sum(map(int, line.split(',')[1:]))/len(line.split(',')[1:])))}"
    out = list(map(lambda_function,input_data))
    return (lambda_function,out)
    # END SOLUTION



def ex5(filename):
    # Complete this function to sort a list of dictionary by 'test3'
    # return the lambda function and the sorted list of dictionaries
    # Use the following code to read JSON file

    import json
    with open(filename) as file:
        grades = json.load(file)
        
    # BEGIN SOLUTION
    lambda_function=lambda row:int(row["test3"])
    return (lambda_function,sorted(grades,key=lambda_function))
    # END SOLUTION

def ex6(input_dict, test_value):
    # Complete this function to find all the keys in a dictionary that map to the input value. 
    # input1: input_dict (dict)
    # input2: test_value
    # output: list of keys
    # BEGIN SOLUTION
    out=[]
    for key, value in input_dict.items():
        if value==test_value:
            out.append(key)
    return out
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
    line_list=[]
    out=[]
    with open(filename) as file:
        for line in file:
            line=line.strip()
            if line!='':
                line_list.append(line)
    for values in line_list:
        try:
            if float(values):
                out.append(values)
        except ValueError:
            continue
    final_val=sorted(out)
    if len(final_val)==0:
        return "The file does not have any valid number to compute the median"
    elif len(final_val)%2!=0:
        return float(final_val[len(final_val)//2])
    else:
        left=float(final_val[len(final_val)//2])
        right= float(final_val[(len(final_val)//2)-1])
        return (left+right)/2

    ### END SOLUTION

def simulateProblem():

    """
    See instructions in exercise_8_instructions.html file
    """
    ### BEGIN SOLUTION
    import random
    game = ["stick","switch"]
    game_random = random.choice(game)
    choice = [1,0]
    rand = random.choice(choice)
    out=[]
    if(game_random=="switch"):
        if(rand==1):
            rand = 0
        else:
            rand = 1
    if(rand==0):
        if(game_random=="stick"):
            out.append(False)
            out.append(False)
        else:
            out.append(False)
            out.append(True)
    else:
        if(game_random=="stick"):
            out.append(True)
            out.append(True)
        else:
            out.append(True)
            out.append(False)
    return out
    ### END SOLUTION


def ex8():
    """
    The function calls the simulateProblem() 10000 times to figure out 
    the empirical (observed) probability of gaining more money when switch 
    and gaining more money when stick to the original choice.
    Return the probability of win due to stick and win due to switch
    """
    ### BEGIN SOLUTION
    stick =0
    switch = 0
    for i in range(10000):
        res=simulateProblem()
        if res[0]==True and res[1]==True:
            stick+=1
        if res[0]==True and res[1]==False:
            switch+=1
    return (stick/10000,switch/10000)
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
    table_data=header

    # data = list(data)
    # for i in range(0, len(data)):
    #     print(data[i])
    #     data[i] = list(data[i])
    
    
    # sort_year = header.index(sort_header_name)
    # data.sort(key=lambda i: i[sort_year],reverse=True)
    
    # max_data = []

    new_data=[]
    for r in data:
        new_data.append(r)
    print(new_data)


    heading_length=[]
    for i in range(len(table_data)):
        heading_length.append(len(str(table_data[i])))
    # print(heading_length)

    record_length=[0]*len(table_data)
    for i in data:
        for j in range(len(i)):
            # print(i[j])
            record_length[j]=max(record_length[j],len(str(i[j])))

    final_len=[]
    final_list=list(zip(heading_length,record_length))
    for i in final_list:
        # print(max(i))
        final_len.append(max(i)+2)
    final_len
    # print(sum(final_len)+ (len(final_len)*2))
    # print(final_len)
    total_len=6+len(data)
    # print(total_len)

    row_outline=''
    for b in final_len:
        row_outline+='+'+('-'*b)
    row_outline+='+'

    rows_cumi=[]
    for t in data:
        rows=''
        for cell in range(len(t)):
            rows+='|'+ f'{t[cell]:^{final_len[cell]}}'
        rows_cumi.append(rows+'|')
    rows_cumi

    title = '|' + f'{title:^{len(row_outline)-2}}' + '|'
    top_border= '-'*len(row_outline)
    header=""
    for headings in range(len(table_data)):
            header+='|'+ f'{table_data[headings]:^{final_len[headings]}}'
    header=header + "|"

    # top_border
    # title
    # row_outline
    # header
    # row_outline
    final_row_list=[top_border,title,row_outline,header,row_outline]

    for row_data in rows_cumi:
        final_row_list.append(row_data)

    final_row_list.append(row_outline)

    final_file = '\n'.join(final_row_list)
    my_file = open(filename, 'w')
    my_file.write(final_file)
    my_file.close()
    # print(final_file)
    ### END SOLUTION