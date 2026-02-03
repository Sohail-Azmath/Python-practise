x = lambda x: x**2
print(x(9))

a = lambda x,y: x+y
print(a(4,9))

b = lambda x:x[0] == 'a'
print(b('apple'))

c = lambda x: 'Even' if x%2 ==0 else 'Odd'
print(c(9))
