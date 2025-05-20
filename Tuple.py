t = ()
print(t)

t= (1,2,3,4) #homogeneous tuple
print(t)

t= (1,2,3,(4,5))
print(t)

t= ("Hello", 1,2,3,4,True)
print(t)

#creating a tuple with one element
t = (1)
print(t)
print(type(t))
# output: <class 'int'>
# to create a tuple with one element, we need to add a comma after the element t = (1,)

t = (1,)
print(t)
print(type(t))
# output: <class 'tuple'>

print("Creating a tuple using a string:")
t = tuple("Goa")
print(t)

print("Creating a tuple using a list:")
t = tuple([1,2,3,4,5])
print(t)

# "Acessing tuple elements"
print("Accessing tuple elements:")
t = (1,2,3,4,5)
print("Accessing first element from the tuple:",t[0])

t = (1,2,3,(4,5))
print("Accessing first element from the nested tuple:",t[3][0])

print("Performing slicing on tuple:")
t = (1,2,3,4,5)
print(t[:3])

# t[0]= 100
# print(t)

'''
    t[0]= 100
    ~^^^
TypeError: 'tuple' object does not support item assignment 

'''

t2 = ()
print(t2)

del t2
# print(t2) 
'''
As we are performing delete operation on the tuple, we cannot access the tuple after deleting it.

'''

#concatinating tuples
t1 = (1,2,3)
t2 = (4,5,6)

#tuple operations
print("Concatenating tuples:")
print(t1+t2)
print("Multiplying tuples:")
print(t1*2)
print("Loops on tuples:")
for i in t1:
    print(i)

# Membership operator
print("Membership operator:")
print(1 in t2)
print(1 not in t2)

# Tuple functions
print("Tuple is:",t2)
print("Length of tuple:",len(t2))
print("Max of tuple:",max(t2))
print("Min of tuple:",min(t2))
print("sum of tuple:",sum(t2))
print("Sorted tuple:",sorted(t2))
print("Sorted tuple in reverse order:",sorted(t2,reverse=True))