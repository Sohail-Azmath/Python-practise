
print("Function to demonstrate local & global variable")
def f(x):
    x =1
    x += 1
    print(x)

x = 5
f(x)
print(x)

print("Function to demonstrate global variable can be accessible inside function")
def g(y):
    print(x)
    print(x+1)

x = 5 #x acts as a global variable
g(x)
print(x)

#New function
def h(x):
    x+=1 

x= 5 #Global variable
h(x)
print(x)



def f(x):
    x = x + 1
    print('in f(x): x =',x)
    return x

x = 3 
z = f(x)
print('in main program: z =',z)
print('in main program: x =',x)
