x = lambda x: x**2
print(x(9))

a = lambda x,y: x+y
print(a(4,9))

b = lambda x:x[0] == 'a'
print(b('apple'))

c = lambda x: 'Even' if x%2 ==0 else 'Odd'
print(c(9))


L = [1,2,3,4,5,6,7,8,9,10]
print(map(lambda x: x**2, L))
y = list(map(lambda x: x**2, L))
print(y)
z = list(map(lambda x: x%2 == 0, L))
print(z)

students = [
    {
        'name': 'John',
        'age': 15,
        'grade': 85
    },
    {
        'name': 'Jane',
        'age': 14,
        'grade': 92
    },
    {
        'name': 'Dave',
        'age': 16,
        'grade': 88
    }
]
y = lambda student: student['name']
print(list(map(y, students)))

x = map(lambda student:student['name'], students)
print(x)


a = list(filter(lambda x: x>4, L))
print(a)

fruits = ['apple', 'banana', 'cherry', 'avocado', 'grape'] 
b = list(filter(lambda fruit: 'e' in fruit, fruits))
print(b)

import functools

sum = functools.reduce(lambda x, y:x+y, L)
print(sum)

L1 = [12,36,11,21,56,58]
max = functools.reduce(lambda x,y: x if x>y else y, L1)
print(max)
min = functools.reduce(lambda x,y: x if x<y else y, L1)
print(min)


l3 = [12,11,21,56,21,45,78,25]
print(functools.reduce(lambda x,y: x if x>y else y, l3))

#List comprehension
l4 = [i**2 for i in range(10)]
print(l4)

l5 = [i**2 for i in L]
print(l5)

fruits = ['apple', 'banana', 'cherry', 'avocado', 'grape'] 
l5 = [fruit for fruit in fruits if fruit[0]=='a']
print(l5)


# Dictionary comprehension
d = { 'Name':'John', 'Age':25, 'City':'New York' }
print(d.items())
d1 = {key:value for key,value in d.items() if len(key)>3}
print(d1)

l = [1,2,3,4,5,6,7,8,9]
d2 = {item:item**2 for item in l if item%2==0}
print(d2)