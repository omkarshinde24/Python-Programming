def remove_and_split(string,word):
    newStr = string.replace(word, "")
    return newStr.strip()


this ="     omkar is good      "
n = remove_and_split(this,"omkar")
print(n)
#print(this)
# print(this.strip())