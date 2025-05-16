x = 5
y = 2
print(x + y) # addition
print(x - y) # subtraction      
print(x * y) # multiplication
print(x / y) # division
print("floor division:",x // y) # floor division
print("modulus:",x % y) # modulus
print("exponent:",x ** y) # exponentiation

# Relational operators
print("Greater than x:",x>y)
print("Smaller than x:",x<y)
print("Equal to x:",x==y)
print("Not Equal to x:",x!=y)
print("Greater than or equal to x:",x>=y)
print("Less than equal to x:",x<=y)

# Logical operators
a = True
b = False
print("Logical AND:",a and b) # Logical AND
print("Logical OR:",a or b) # Logical OR
print("Logical NOT:",not a) # Logical NOT

# Bitwise operators
a = 2  # Output: 0b10
b = 3  # Output: 0b11
print("Bitwise AND:",a&b)
print("Bitwise OR:",a|b)
print("Bitwise XOR:",a^b)
print("Bitwise NOT:",~a)
print("Left Shift:",a<<1)
print("Right Shift:",a>>1)
print("complement:",~a)

# Assignment operators
a = 5
print("Assignment operator:",a)
a += 2 # a = a + 2
print("Assignment operator with '+' sign:",a)
a -= 2 # a = a - 2
print("Assignment operator with '-' sign:",a)
a *= 2 # a = a * 2
print("Assignment operator with '*' sign:",a)
a /= 2 # a = a / 2
print("Assignment operator with '/' sign:",a)

# a++ or ++a 
# Both are not valid in python

# Identity Operators
a = 10
b = 10
print(a is b)

a= [1,2,3]
b = [1,2,3]
print(a is b) # False because a and b are different objects

x = "Delhi"

print("D" not in x)