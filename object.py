def f(num):
    return num ** 2

print(f(2))  #-> gives 4 as output
x = f #aliasing function f to x
print(x(2)) #-> gives 4 as output

#deleting a function
del f
print(x(2)) #-> gives 4 as output

l = [1, 2, 3, 4]
print(l)

#storing the function in a list
l = [1,2,3,4,x]
print(l)

#Accessing the function from the list
print(l[-1](3))

l = [1,2,3,4,x(4)]
print(l)

# Example 1:
def func_a():
    print('inside func_a')

def func_c(z): #we pass func_a as a argument fo the func_c
    print('inside func_c')
    return z() # function z is function func_a

print(func_c(func_a))

# Example 2:
def f():
    def x(a,b):
        return a + b
    return x

val = f()(3,2) # f() returns the function x, which is then called with arguments 3 and 2
print(val)

