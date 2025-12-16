import FunDemo

c = FunDemo.check_number(50)
print(c)

#Default Arguments Demonstration
def power(a, b):
    return a ** b

power(2,3)

'''
power(2)  # This will raise a TypeError because b is missing
power()  # This will raise a TypeError because both a and b are missing

Traceback (most recent call last):
  File "E:\\vs_code\\Practise python\\Functions.py", line 11, in <module>
    power(2)  # This will raise a TypeError because b is missing
    ^^^^^^^^
TypeError: power() missing 1 required positional argument: 'b'

Note: Here we have specified the path with \\. This is beacause in Python, \p acts an invalid escape sequence. To avoid this, we use double backslashes (\\) to represent a single backslash in the file path.

'''
#Triple quotes (''' or """) create a string, not a comment.

def power(a =1, b = 1):
    return a ** b

power(2) # demonstrating single default argument. The output will be 2^1 = 2.
power() # demonstrating both default arguments. The output will be 1^1 = 1.
power(2,3) #demonstating positional Arguments. The output will be 2^3 = 8.

power(b = 4, a = 3) # demonstrating keyword arguments. The output will be 3^4 = 81.

#Arbitrary Arguments Demonstration
def felxi(*number): #Here the asterisk (*) before number allows the function to accept any number of positional arguments as a tuple.
    product = 1
    print(number)
    print(type(number))
    for i in number:
        product = product * i
    print(product)
    
felxi(1,2,3) # passing 3 arguments
felxi(4,5)   # passing 2 arguments

