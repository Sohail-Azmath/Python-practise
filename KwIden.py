import keyword

print(keyword.kwlist)


# Identifiers
name = 'Mohammed'
print(name)

_ = 'Sohail Azmath'
print(_)

# $ = 'Sohail Azmath'
# print($)
#           $ = 'Sohail Azmath'
#     ^
# SyntaxError: invalid syntax

# Input function
first = int(input("Enter your place:"))
second = int (input("Enter your name:"))
print(first)
print(second)
print(first + second)

print(type(first))
print(type(second))

# implicit & explicit conversion

# a=int('4.5')
# print(a)

#  File "E:\vs code\Practise python\Kwiden.py", line 31, in <module>
#     a=int('4.5')
# ValueError: invalid literal for int() with base 10: '4.5'

