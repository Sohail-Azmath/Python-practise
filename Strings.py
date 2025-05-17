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

print("String functions")

s = "kolkata"
print("Length of the string:",len(s))
print("Maximum character in the string:",max(s))
print("Minimum character in the string:",min(s))
print("Sorted order of characters in the string:",sorted(s))
print("Reversed order of characters in the string:",sorted(s, reverse = True))
print("Capitalized string:", s.capitalize())
tr = "Title of the project"
print("Title of the project:", tr.title())
print("Upper case of the string:", s.upper())
print("Lower case of the string:", s.lower())
print("Swapped case of the string:", s.swapcase())
print("counting the frequency of a character:",s.count("k"))
print("finding the character in the string:",s.find("k"))
print("finding the character in the string:",s.index("k"))
print("Hello, I'm {}. I'm {} years old.".format("Mohammed Sohail Azmath", 20))
print("Hello, I'm {1}. I'm {0} years old.".format("Mohammed Sohail Azmath", 20))
print("Hello, I'm {name}. I'm {age} years old.".format(name="Mohammed Sohail Azmath", age =20))
print("Hello, I'm {name}. I'm {weight} years old.".format(name="Mohammed Sohail Azmath", weight=65, age = 20))

C = "FLAT20"
print("check for alphabet and numeric:", c.isalnum())
d = "FLAT"
print("check for alphabet:", d.isalpha())
e = "450"
print("check for digit:", e.isdigit())
g = "Hello_world"
print("check for float:", g.isidentifier())

