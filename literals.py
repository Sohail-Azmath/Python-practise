a = list('Hello')
print(a)

# Numeric literals
a = 0b1010 #Binary "0b" represent Binary notation
b = 100 #Decimal
c = 0o310 #Octal "0o" represent Octal notation
d = 0x12C #Hexadecimal "0x" represent Hexadecimal notation
print(a, b, c, d)

# float literals
float_num = 1.5 #Decimal
float_1= 1.5e2 #Scientific notation "e2" represent exponent i.e. 1.5 * 10^2
float_2= 1.5e-2 #Scientific notation "e-2" represent exponent i.e. 1.5 * 10^-2
print(float_num, float_1, float_2)

# complex literals
x = 5j
y = 3 + 4j
print(x, y)
print(y.real, y.imag) # real and imaginary part of complex number where x.real is real part and x.imag is imaginary part

# string literals
str_1 = 'Hello World' # Single quotes 
str = "Hello World" # Double quotes 
str_2 = '''Hello World''' # Triple quotes
str_3 = """Hello World"""
print(str, str_1, str_2, str_3)

unicode = u"\U0001f600" #unicode string can be accepted by python. "u" is specified before the unicode.
print(unicode)

raw_Str = r"Hello \n World" # raw string. "r" is specified before the string.
print(raw_Str)

# boolean literals
a = True + 1
b = False + 50
print(a, b) # True is 1 and False is 0

