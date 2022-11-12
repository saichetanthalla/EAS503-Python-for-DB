class IteratorClass:
    # Complete this class! It takes in three inputs when initializing.
    # input#1 x -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#2 y -- is a sequence, either a list or a tuple. Raise a ValueError if it is not a list or a tuple
    # input#3 operator -- is a string that can either be 'add', 'sub', 'mul', 'div' -- If the specified operator
    # is not one of these, raise a ValueError.

    # Complete the class by writing functions that will turn it into an iterator class.
    # https://www.programiz.com/python-programming/methods/built-in/iter
    # The purpose of the class is to take two lists(x and y), apply the specified operator and return the output
    # as an iterator, meaning you can do "for ele in IteratorClass(x,y,'add')"
    # NOTE: For the / operator, round to two decimal places
    # Raise ValueError when the length is not the same for both inputs
    # Raise ValueError when the operator is not add, sub, mul, or div.

    # BEGIN SOLUTION
    
    # BEGIN SOLUTION
    def __init__(self,x,y,operator):

        self.max=len(y)
        self.result=[]
        if((type(x) in [list,tuple]) and (type(y) in [list,tuple]) and operator in ["add","div","mul","sub"]) and (len(x)==self.max):
            match operator:                              
                case "add": 
                    for a, b in zip(x,y):
                        self.result.append(a + b)
                case "sub": 
                    for a, b in zip(x,y):
                        self.result.append(a - b)
                case "mul":
                    for a, b in zip(x,y):
                        self.result.append(a * b)
                case "div":
                    for a, b in zip(x,y):
                     self.result.append(round(a/b,2))                                                   
        else:         
            raise ValueError
        
    def __iter__(self):
        self.i = -1
        return self
    
    def __next__(self):
        if(self.i >= self.max-1):
            raise StopIteration
        self.i += 1
        return self.result[self.i]
    # END SOLUTION


class ListV2:
    # Complete this class to fulfill the following requirement
    # 1) The class only takes one input argument which is a list or a tuple;
    #    Raise ValueError if the input is not a list or tuple
    # 2) The class overload loads +,-,*,/ and returns a ListV2 object as the result
    # 3) The class can handle +,-,*,/ for both list and int/float, meaning the thing to the right of the operator
    #    can be a sequence or a number;
    # 4) The class is an interator class
    # 5) The class has a __repr__ method that should show all the values in the class as [...]
    # HINT: Study the assert statements below to understand how this class is being used and reverse engineer it!
    # NOTE: For the / operator, round to two decimal places


    # BEGIN SOLUTION
    def __init__(self, input1):
        self.input1 = input1
      
        if (type(input1) is not list) and (type(input1) is not tuple):
            raise ValueError
 
    def __add__(self, input2):
        result=[]
        if (type(input2) is int) or (type(input2) is float):
            for i in self.input1:
                out= i+input2
                result.append(out)
        else:
            for i,j in zip(self.input1,input2):
                out=i+j
                result.append(out)
        return ListV2(result)
    
    def __sub__(self, input2):
        result=[]
        if (type(input2) is int) or (type(input2) is float):
            for i in self.input1:
                out=i-input2
                result.append(out)
        else:
            for i,j in zip(self.input1,input2):
                out=i-j
                result.append(out)
        return ListV2(result)
    
    def __mul__(self, input2):
        result=[]
        if (type(input2) is int) or (type(input2) is float):
            for i in self.input1:
                out=i*input2
                result.append(out)
        else:
            for i,j in zip(self.input1,input2):
                out=i*j
                result.append(out)
        return ListV2(result)
    
    def __truediv__(self, input2):
        result=[]
        if (type(input2) is int) or (type(input2) is float):
            for i in self.input1:
                out=i/input2
                result.append(round(out,2))
        else:
            for i,j in zip(self.input1,input2):
                out=i/j
                result.append(round(out,2))
        return ListV2(result)
    
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if(self.num >= len(self.input1)):
            raise StopIteration
        result = self.input1[self.num]
        self.num += 1
        return result
    
    def __repr__(self):
        return str(self.input1)
    
    # END SOLUTION