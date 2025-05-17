# Creating Strings

c= 'Hello World'
print("Using single inverted commas:",c)

c = "Hello World"
print("Using double inverted commas:",c)

c= """Hola"""
print("Using triple inverted commas:",c)

c= str("This is type conversion")
print("using type conversion:",c)

b = "Hello world"
print(len(b))
print(b[6])

print(b[-1])

print(b[0:5])
print(b[:5]) # we just indicate the end index. We obtain the substring till that index from the start
print(b[6:]) # we indicate the start index. We get a substring till end from the specified start index.
print(b[:])
print(b[0:5:2]) # we indicate the start index, end index and the step value. We get a substring from start to end with the specified step value.
print(b[-5:-1:2])
print(b[::-1])
print(b[-1:-5:-1])

c= "Hello"
# c[0] ="X"
# print(c)
c= "welcome"
print(c)

'''
del c[0]
print(c)

del c
print(c)

del c[0:5]
print(c)

# all the above deletion operation on string are not possible as strings are immutable.

'''

print("Hello" + "-" + "World")
print("Hello" * 3)

print("Gidda " == "Baghra")
print("Gidda" != "Baghra")
print("Gidda" > "Baghra") #Here the comparison of strings takes place in Lexographical order.
print("Gidda" < "Baghra") #Here the comparison of strings takes place in Lexographical order.
print("Logical Operators")
print(bool("" and "Hello"))
print(bool("" or "Hello"))
print(bool("Gidda" and "Baghra"))
print(not "")
print(not "Hello")

print("Loops in Strings")
c = "Hello-world"
for i in c[::]:
    print(i)
    
print("H" in c)
print("Gidda" in c)
print("Hello" not in c)

