#Create empty set
s = set()

#Add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

#Add duplicated element
s.add(3)
print(2)

#Remove element from the set
s.remove(2)
print(s)

#Formmated string
print(f"The set has {len(s)} elements.")
