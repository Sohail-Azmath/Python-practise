s = {}
print(type(s))

s = set()
print(type(s))

s1 = {1, 2, 3}
print("Homogenous sets:",s)

s = {"hello", 1, 2, 3,4}
print("Heterogenous sets:",s)

s2 = {1,1,2,2,3,4,5}
print("Set with duplicates:",s2)

print("Using tuple & list as a element in set:")
print("Using tuple in set:",{(1,2,3,3),4,5,6})
# print("Using list in set:",{[1,2,3,4], 5,6,7})
print("Creating 2D or 3D sets:")
# s = {{1},{2},4,5}
# print("2D set:",s)

print("Accessing set elements:")
# print("Accessing element through positive indexing:",s2[0])
# print("Accessing element through negative indexing:", s2[-1])
# print("Accessing element through slicing:",s2[0:3])

print("Editing set elements:")
s = {1,2,3,4}
print("Set before changing element using list :",s)
print("Address of set:",id(s))
# Addressing of set: 2469272447776
l1 = list(s)
print("list of set :",l1)
l1[0]=100
s = set(l1)
print("Set after changing element using list:",s)
print("Address of set:",id(s))
# Addressing of set: 2469272158944

# Hence we see there is a difference in the address of set before and after changing the element using list. This is against the defination of editing the set. 

# NOTE: Editing is considered when the memory location is same.

s.add(200)
print("Set after adding element:",s)

print("deleting a set s1")
del s1
# print("Set after deleting element:",s1)

s.remove(200)
print("Set after removing element:'200'",s)

s.pop()
print("Set after popping element:",s)
# here the pop operation delete the element based on hashing function.

# operations on set
s1 = {1,2,3}
s2 = {4,5,6}
'''
print("Using concatenation operator:",s1+s2) # we cannot use + operator on set
TypeError: unsupported operand type(s) for +: 'set' and 'set' 
'''

'''

print("using multiplication operator:",s1*3)
# we cannot use * operator on set
TypeError: unsupported operand type(s) for *: 'set' and 'int'

'''


print("Using loop to print:")
for i in s1:
    print(i)

print(1 in s1)
print(1 not in s1)

print("Length of set :", len(s1))
print("Maximum element in set:", max(s1))   
print("Minimum element in set:", min(s1))
print("Sum of set elements:", sum(s1))
print("Sorted set elements:", sorted(s1))
print("sorted set elements in reverse order:", sorted(s1,reverse=True))

print(s1)
print(s2)
print("Union of two sets:",s1.union(s2))
print("intersection of two sets:",s1.intersection(s2))
print("difference of two sets:",s1.difference(s2))
print("Difference of two sets:",s2.difference(s1))
print("Disjoint sets:",s1.isdisjoint(s2))
print("Subset of set:",s1.issubset(s2))
print("Superset of set:",s1.issuperset(s2))