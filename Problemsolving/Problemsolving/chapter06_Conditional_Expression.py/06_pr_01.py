num1 = input(("Enter number 1:"))
num2 = input(("Enter number 2:"))
num3 = input(("Enter number 3:"))
num4 = input(("Enter number 4:"))

if(num1>num4):
    f1 = num1
else:
    f1 = num4
if(num2>num3):
    f2 = num2
else:
    f2 = num1

if(f1>f2):
        print(str(f1) + "is greatest")
else:
        print(str(f2) + "is greatest")