print("Creating a list:")
l =[] # empty list
print(l)

a = [1,2,3,4,5] #homogeneous list
print(a)

b = [1, "Hello", 8.6, True, 8+9j] # heterogeneous list
print(b)

#Multi- Dimensional list
# 2D list
d = [1,2,3,[6,7],[8,9]]
print("2D list:",d)

#3D list
b3 =  [2,3,4,[[8,9],[0,3]],5,6,7,[[7,6],[4,3]]]
print("3D list:",b3)

#Type conversion
ty = list("Hello")
print("Type conversion list:",ty)

#accessing elements in the list
print("Accessing elements in the 1D - list:", a[0])
print("Accessing elements in the 2D - list:", d[-1][0]) #The last element in the d list is: [8,9]. let's store the last element in a variable and access the elements in it.
#last = [8,9]
# to access the element in the "last" list, we can use the index of the element in the last list. i.e. last[0]= 8, last[1]=9.

#Similarly, we can access the elements in the 3D list.
print("Accessing elements in the 3D - list:", b3[3][0][1]) #The last element in the b3 list is: [[7,6],[4,3]]. let's store the last element in a variable and access the elements in it.
#last = [[7,6],[4,3]]
# to access the element in the "last" list, we can use the index of the element in the last list. i.e. last[0]= [7,6], last[1]=[4,3].
print("List before editing:",b)
b[1] = "200"
print("Updating the list:",b)
b[1:3] = [4,5,6]
print("operation slicing on list b:",b)
b[-1] = "Hello"
print("Perfroming edit opertion using negative indexing:",b)

print("List extensions:")
b.append("world")
print("Appending a list:",b)
b.extend("Goa")
print("extending list using extend method:",b) #Here the string is converted into list and then appended to the list. Note: Append operation add multiple elements to the list.
b.extend([100,400,500])
print("adding more than one element:",b)
b.insert(1,"complex")
b.insert(3, 4+5j)
print("Modifying list using insert operation:",b)

print("Deleting the elements using del keyword in the list:")
del b[2]
print("Deleting the element at index 2:",b)
print("Deleting the series of elements in the list:")
del b[-6:-3]
print("Deleting the elements in the list:",b)
b.remove(5)
print("Deleting the element using remove method:",b)
b.pop()
print("Deleting the last element in the list:",b)
b.clear()
print("Deleting all the elements in the list:",b) #this gives an empty list.

# concatenation of list
print("Concatenation of list:", a+d)

print("Multiplication of list:", a*2)
for i in a:
    print(i)

# Functions in list
print("Length of the list:", len(a))
print("Maximum element in the list:", max(a))
print("Minimum element in the list:", min(a))
print("Sorted in list:", sorted(a))
print("Finding the index of the element in the list:", a.index(3))
a.sort()
print("sort this is the permanent operation:",a)

