myDict = {
    "Fast":"In a Quick Manner",
    "Harry":"A coder",
    "Marks":[1,2,3],
    "anotherdict":{'omkar':'player'},
    
}

print(list(myDict.keys()))  # Prints the list  of the dictionary
print(myDict.values()) # Prints the values of the dictionary
print(myDict.items()) # Prints the (key,value) for all contents of the  dictionary
print(myDict)
updateDict = {
    "lovish":"friend"
}

myDict.update(updateDict) #Updates the dictionary by adding key value pairs from updateDict
print(myDict)