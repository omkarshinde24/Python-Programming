#Creating an empty set

b = set()
print(type(b))

#  adding values to an empty set
b.add(4)
b.add(5)
b.add(4)
b.add(5)
b.add(4)
b.add(5) # Adding a value repeatedly does not change a set
b.add((4,5,6))
#b.add({4:5}) #Cannot add list or dictionary to sets

print(b)
print(len(b)) #length of the set
b.remove(5) # remove the 5
print(b)

print(b.pop())
print(b)

