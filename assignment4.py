def ex1(password):
    # In this exercise you will complete this function to determine whether or not
    # a password is good. We will define a good password to be a one that is at least
    # 8 characters long and contains at least one uppercase letter, at least one lowercase
    # letter, at least one number, and at least one of the following special characters (!, @, #, $, ^).
    # This function should return True if the password
    # passed to it as its only parameter is good. Otherwise it should return False.
    #
    # input: password (str)
    # output: True or False (bool)
    # BEGIN SOLUTION
    up=0
    down=0
    spec=0
    num=0
    le=0
    sp=["!", '@', "#", "$", "^"]
    nu=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(password)>=8:
        le+=1
    for i in password:
        if i.upper()==i:
            up+=1
        if i.lower()==i:
            down+=1
        if i in sp:
            spec+=1
        if i in nu:
            # print(i)
            num+=1
    # print(le,up,down,spec, num)
    if le>0 and up>0 and down>0 and spec>0 and num>0:
        return True
    else:
        return False
    # END SOLUTION


def ex2(sentence):
    # Complete this function to calculate the average
    # word length in a sentence
    # Input: sentence
    # Output: average word length in sentence
    # Hint: count punctuations with whatever word they are `touching`
    # Hint: round the average to two decimal places
    # BEGIN SOLUTION
    cumilative_length=0
    sentence=sentence.split()
    for word in sentence:
        cumilative_length+=len(word)
    ans=cumilative_length/len(sentence)
    return round(ans,2)
    # END SOLUTION


def ex3(filename):
    # Complete this function to count the number of lines, words, and chars in a file.
    # Input: filename
    # Output: a tuple with line count, word count, and char count -- in this order

    # BEGIN SOLUTION
    line_count=0
    word_count=0
    chars_count=0
    with open(filename) as file:
        for line in file:
            line_count+=1
            chars_count+=len(line)
            line=line.split()
            word_count+=len(line)
            
    return (line_count,word_count,chars_count)


    # END SOLUTION


def ex4(apr):
    # Complete this function to use a while loop to determine how long it takes for an investment
    # to double at a given interest rate. The input to this function, apr, is the annualized interest rate
    # and the output is the number of years it takes an investment to double. Note: The amount of the initial
    # investment (principal) does not matter; you can use $1.
    # Hint: principal is the amount of money being invested.
    # apr is the annual percentage rate expressed as a decimal number.
    # Relationship: value after one year is given by principal * (1+ apr)

    # BEGIN SOLUTION
    principal=1
    check=principal*2
    after_one_year=0
    while principal<check:
        principal=principal * (1+ apr)
        after_one_year+=1
    return (after_one_year)

    # END SOLUTION


def ex5(n):
    # Complete this function to return the number of steps taken to reach 1 in
    # the Collatz sequence (https://en.wikipedia.org/wiki/Collatz_conjecture)

    # BEGIN SOLUTION
    if n==1:
        return 0
    steps=0
    while n!=1:
        if n%2==0:
            steps+=1
            n=n/2
        else:
            steps+=1
            n=(n*3)+1
    return steps
    # END SOLUTION


def ex6(n):
    # A positive whole number > 2 is prime if no number between 2 and sqrt(n)
    # (include) evenly divides n. Write a program that accepts a value of n as
    # input and determine if the value is prime. If n is not prime, your program should
    # return False (boolean) as soon as it finds a value that evenly divides n.
    # Hint: if number is 2, return False

    # BEGIN SOLUTION
    res = []
    import math
    if n==2:
        return False
    elif int(math.sqrt(n)) < 2:
        if n%2!=0:
            return True
    
    for i in range(2,int(math.sqrt(n))+1):
# for i in range(2,n):

        if n%i==0 :
            res.append(0) 
        else :
            res.append(1)
    
    if 0 in res :
        return False
    if 1 in res :
        return True

    

    # return True 



    # END SOLUTION


def ex7(n):
    # Complete this function to return all the primes as a list less than or equal to n
    # Input: n
    # Output: a list of numbers
    # hint use ex6

    # BEGIN SOLUTION
    ans=[]
    for i in range(2,n+1):
        if ex6(i):
            ans.append(i)
    return ans

    # END SOLUTION


def ex8(m, n):
    # Complete this function to determine the greatest common divisor (GCD).
    # The GCD of two values can be computed using Euclid's algorithm. Starting with the values
    # m and n, we repeatedly apply the formula: n, m = m, n%m until m is 0. At this point, n is the GCD
    # of the original m and n.
    # Inputs: m and n which are both natural numbers
    # Output: gcd

    # BEGIN SOLUTION
    while n != 0:
        m,n = n, m % n
    return m
    # END SOLUTION


def ex9(filename):
    # Complete this function to read grades from a file and determine the student with the highest average
    # test grades and the lowest average test grades.
    # Input: filename
    # Output: a tuple containing four elements: name of student with highest average, their average,
    # name of the student with the lowest test grade, and their average. Example ('Student1', 99.50, 'Student5', 65.50)
    # Hint: Round to two decimal places

    # BEGIN SOLUTION
    student_1_name=[]
    student_1_avg=[]
    summation=0
    with open(filename) as file:
        for line in file:
            summation=0
            if line.strip():
                line=line.split(",")
                number_course=len(line)-1
                for data in line[1:]:
                    summation+=int(data)
                avg=summation/number_course
                student_1_name.append(line[0])
                student_1_avg.append(avg)
        t=student_1_avg.index(max(student_1_avg))
        s=student_1_avg.index(min(student_1_avg))
        return((student_1_name[t],student_1_avg[t],student_1_name[s],student_1_avg[s]))     

    # END SOLUTION


def ex10(data, num_outliers):
    # When analyzing data collected as a part of a science experiment it
    # may be desirable to remove the most extreme values before performing
    # other calculations. Complete this function which takes a list of           
    # values and an non-negative integer, num_outliers, as its parameters.
    # The function should create a new copy of the list with the num_outliers
    # largest elements and the num_outliers smallest elements removed.
    # Then it should return teh new copy of the list as the function's only
    # result. The order of the elements in the returned list does not have to
    # match the order of the elements in the original list.
    # input1: data (list)
    # input2: num_outliers (int)

    # output: list

    # BEGIN SOLUTION
    data.sort()
    # ans=[]
    # max_out=data[:2]
    # min_out=data[-2:]
    # for i in data:
    #     if i not in max_out and i not in min_out:
    #         ans.append(i)
    return(data[2:-2])
    # return data[num_outliers:-num_outliers]
    # END SOLUTION


def ex11(words):
    # Complete this function to remove duplicates from the words list using a loop
    # input: words (list)
    # output: a list without duplicates
    # MUST USE loop and NOT set!
    # Preserve order

    # BEGIN SOLUTION
    temp=[]
    for i in words:
        if i not in temp:
            temp.append(i)
    return temp            
    # END SOLUTION


def ex12(n):
    # A proper divisor ofa  positive integer, n, is a positive integer less than n which divides
    # evenly into n. Complete this function to compute all the proper divisors of a positive
    # integer. The integer is passed to this function as the only parameter. The function will
    # return a list of containing all of the proper divisors as its only reult.

    # input: n (int)
    # output: list

    # BEGIN SOLUTION
    ans = []
    for i in range(1,n):
        if (n%i)==0:
            ans.append(i) 
    return ans
    # END SOLUTION


def ex13(n):
    # An integer, n, is said to be perfect when the sum of all of the proper divisors
    # of n is equal to n. For example, 28 is a perfect number because its proper divisors
    # are 1, 2, 4, 7, and 14 = 28
    # Complete this function to determine if a the number a perfect number or not.
    # input: n (int)
    # output: True or False (bool)

    # BEGIN SOLUTION
    if sum(ex12(n))==n:
        return True
    else:
        return False
    # END SOLUTION


def ex14(points):
    # Complete this function to determine the best line.
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/line-of-best-fit
    # input: points (list of tuples contain x, y values)
    # output: (m, b) # round both values to two decimal places

    # BEGIN SOLUTION
    x=[]
    y=[]
    for point in points:
        x.append(point[0])
        y.append(point[1])
    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    slope_list_num=[]
    slope_list_den=[]
    for i in range(len(x)):
        slope_num=(x[i]-x_mean)*(y[i]-y_mean)

        slope_list_num.append(slope_num)
        slope_den=((x[i]-x_mean)**2)
        slope_list_den.append(slope_den)
    slope=sum(slope_list_num)/sum(slope_list_den)
    y_intercept=y_mean - (slope*x_mean)
    return (round(slope,2),round(y_intercept,2))
    # END SOLUTION


def ex15(title, header, data, filename):
    # This problem is hard.
    # Open up ex15_*_solution.txt and look at the output based on the input parameters, which
    # can be found in the test_assignment4.py file
    # Function inputs: 
    # title -- title of the table -- a string
    # header -- header of the table  -- a tuple
    # data -- rows of data, which is a tuple of tuples
    # filename -- name of file to write the table to
    # Your job is to create the table in the file and write it to `filename`
    # Note that you need to dynamically figure out the width of each column based on 
    # maximum possible length based on the header and data. This is what makes this problem hard. 
    # Once you have determined the maximum length of each column, make sure to pad it with 1 space
    # to the right and left. Center align all the values. 
    # OUTPUT: you are writing the table to a file

    # BEGIN SOLUTION
    table_data=header
    heading_length=[]
    for i in range(len(table_data)):
        heading_length.append(len(str(table_data[i])))
    heading_length

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
    








# final_table= 




    # END SOLUTION