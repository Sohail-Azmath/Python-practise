
from sympy import subsets


a, b = map(int, input().split())

res = 0
for _ in range(b):
    res += a

print(res)


def multiply(a, b):
    res = 0
    for i in range(b):
        res += a
    return res

print(multiply(3, 4))


def multi(a,b):
    if b == 1:
     return a
    else:
     return a + multiply(a,b-1)

print(multi(3,4))

#Factorial code
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

def palindrome(str):
    if len(str) == 1:
      return True
    else:
        if str[0] == str[-1]:
           return palindrome(str[1:-1])
        else:
            return False
        
print(palindrome("Enviroment"))
#the above code fails for the even length of the string. To overcome this we make slight changes i.e. if len(str) <= 1: -> return True. 
# The above changes ensures that this will work for both even and odd length of strings.
def palin(str):
    if len(str) <= 1:
      return True
    else:
        if str[0] == str[-1]:
            return palin(str[1:-1])
        else:
            return False

print(palin("noon"))

# Rabbit Problem
# Using iterative method
n = int(input())
a = 0; b = 1; c = 0
while(n!=0):
   c = a+ b
   a = b
   b = c
   n -= 1
print(c)

# Using Recursion


def rab(n):
   if n == 0 or n ==1:
      return 1
   else:
      return rab(n - 1) + rab(n - 2)
      
print(rab(9))


def lst(l):
    subsets = [] 
    
    for i in range(len(l)):
        ele = l[i]
        new_subsets = []
        for s in subsets:
            temp = s.copy()
            temp.append(ele) 
            new_subsets.append(temp)
            subsets = subsets + new_subsets
    print(subsets)
   
lt= list(int(input()) for _ in range(3))
lst(lt)
print(lt)