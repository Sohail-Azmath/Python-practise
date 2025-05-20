sample = "how are you?"
l = []
print(sample.split())
for i in sample.split():
    print(i)
    l.append(i.capitalize())
print(l)    
print(" ".join(l))

trying = "Today is a good day"
print(trying.split())
l2 = []
for i in trying.split():
    print(i)
    l2.append(i.capitalize())

print(l2)
print(" ".join(l2))

str = "abc@gmail.com"
print(str.startswith("abc"))

print(str.index("@"))
print(str[:3])

lst = [1,1,2,2,3,3,4,4]
s = set(lst)
print(s)
l2 = []
for i in lst:
    if(i not in l2):
        l2.append(i)

print(l2)
