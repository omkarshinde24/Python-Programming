sub1 = int(input("Enter first sub marks\n"))
sub2 = int(input("Enter second sub marks\n"))
sub3 = int(input("Enter third sub marks\n"))
sub4= int(input("Enter fourth sub marks\n"))

if(sub1<33 or sub3<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subject")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total persentage less than 40")
else:
    print("Congratulations You passed the Exam")
