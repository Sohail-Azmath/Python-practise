# help("modules")

import math
print("Square root of 16:",math.sqrt(16))

print("Ceiling value of 5.4:",math.ceil(5.4))
print("Floor value of 5.4:",math.floor(5.4))
print("Factorial of 5:",math.factorial(5))
print("Pi value:",math.pi)
print("Exponential value of e:",math.e)

import random
print("creating a random number between 1 and 100:",random.randint(1,100))

a=[1,2,3,4,5]
random.shuffle(a)
print("creating a shuffle of list:",a)

import time
print("Time span", time.time())
print("See time:",time.ctime())
print("hello")
time.sleep(5)
print("world")

import os
print("Current working directory:",os.getcwd())
print("List of files in current directory:",os.listdir())