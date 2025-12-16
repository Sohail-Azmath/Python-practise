# we create a function to determine the odd & even number
def check_number(number):
    '''
    This is a function which determine the number is even or odd.
    input - any interger
    output - Even/Odd
    create by -  xyz
    last edited - 02-06-2025

    '''
    if type(number) == int:
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Wrong parameter"
   
    
# for i in range(1,11):
#     print(f"Given number {i} is:{check_number(i)}")
