# Creating a Dictionary

d = {} #Empty Dictionary
print("Empty Dictionary created:",d)

d = {"Name":"Sohail", "Age":28}
print("Instance of a Dictionary:",d)

# Proving Rule 3
'''

# d = {[1,2,3]:"Names"}
print("Assigning key values by list:",d)
# TypeError: unhashable type: 'list'

'''

d = {(1,2,3):"Sohail"}
print("Assigning tuple as key vale in Dictionary:")

# Proving rule 4

d={"Name":"Maaz", "Name":"Meraj"}
print("Proving keys in dictionary takes only one key value:",d)

# Output:  {'Name': 'Meraj'}

# Multi dimensional dictionary
d = {"Name":"Anonymous","Standard":"Class 12","Marks":{"2A":42,"2B":36,"ENG":78}}
print("Nested dictionary:",d)

# proving rule 1
# Access items from a dict
print("Accessing values from the dictionary is done using keys")
print("name value in dict:",d["Name"])
print("Accesing elements in Nested Dictionary:",d["Marks"])
# we are able to access marks here. If we want to access marks of particular subject we use similar indexing like 2D array.
print("Accessing elements in the nested dictionary: English Marks:",d["Marks"]["ENG"])
d["Name"] = "Famous"
print("Editing the values of a dictionary using key:",d)

print("Accessing dictionary value using get function:",d.get("Name"))

'''
print("Accessing dictionary value using get function:",d.get("M2"))
Accessing dictionary value using get function: None
'''

print("Adding key-value pair to the dictionary:")
d["Age"]=45
print("Dictionary d after adding a key-value pair:",d)

# Adding the element to the 2D dictionary
d["Marks"]["M2"]=52
print("Adding element to the 2D dictionary:",d)

# Using Del keyword
del d["Age"]
print("Dictionary after deleting a element:",d)

# Loops in the dictionary
for i in d:
    print(i)

for i in d:
    print(i, d[i])

# Membership operator
print("Checking the key in the dictionary:", "Name" in d)

# Functions
print("Length of dictionary:",len(d))
print("Minimum value in the dictionary:",min(d))
print("Maximaum value in the dictionary:",max(d))

print("Keys in the dictionary:", d.keys())
print("Values in the dictionary:",d.values())