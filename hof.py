# Higher Order function

# Q. We are given a list of elements. We are required to find the sum of elements divisible by 3, sum of odd and sum of even numbers in the list. 

def return_sum(l):
    odd_sum = 0
    even_sum = 0
    div_sum = 0
    for i in l:
        if i % 2 == 0:
            even_sum += i
        if i % 2 != 0: 
            odd_sum += i
        if i % 3 == 0:
            div_sum += i
    return(odd_sum, even_sum, div_sum)

l = [1,2,3,4,5,6,7,8,9]
odd_sum, even_sum, total_sum = return_sum(l)
print(odd_sum,even_sum, total_sum)

#converting the above function to higher order function

def return_sum_hof(l, func):
    total_sum = 0
    for i in l:
        if func(i):
            total_sum += i
    return total_sum

l = [1,2,3,4,5,6,7,8,9]
x = lambda x: x % 2 == 0
y = lambda y: y % 2 != 0
z = lambda z: z % 3 == 0

print(return_sum_hof(l, x))  # even sum
print(return_sum_hof(l, y))  # odd sum  
print(return_sum_hof(l, z))  # sum of elements divisible by 3

l = [1,2,3,4,5,6,7,8,9]
print(map(lambda x: x**2, l))
y = list(map(lambda x: x**2, l))
print(y)
z = list(map(lambda y: y%2 == 0, l))
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


a = list(filter(lambda x: x>4, l))
print(a)
