number = int(input("Enter a number: "))
i = 1

while i<11:
    print(number,"*",i,"=",number * i)
    i+=1

# for(int i = 0;i<n;i++){
#     print(i);
# }
# This is the for loop in other languages
a = list(range(1,10))
print("List range upto to 10:",a)

b = list(range(5))
print("List range upto 5:",b) #Here the start number is choosen as 0 and end number is 4.

c= list(range(1,10,2))
print("List range with step parameter:",c) #Here the start number is choosen as 1 and end number is 5 and step is 2(difference betweeen two consecutive numbers).

d = list(range(10,0,-1))
print("List for reverse printing:",d)

for i in range(1,10):
    print("range upto 10 numbers:",i)

for i in "kolkata":
    print("for loop in sequence of characters:",i)

for i in ["kolkata","Delhi","Mumbai"]:
    print("for loop in sequence of strings:",i)

for i in (1,2,3,4,5):
    print("for loop in sequence of numbers in a tuple:",i)

for i in {1,2,3,4,5}:
    print("for loop in sequence of numbers in a set:",i)


# printing a star sequence

rows = int(input("Enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(0,i):
        print("*",end=" ")
    print("")

