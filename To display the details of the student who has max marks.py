num=int(input("enter how many number do you want in list:"))
lst1=[]
lst2=[]
lst3=[]
for i in range(num):
    name=input("enter the name:")
    roll=int(input("enter the roll number:"))
    marks=int(input("enter the marks:"))
    lst1.append(name)
    lst2.append(roll)
    lst3.append(marks)
max=lst3[0]
for i in lst3:
    if i>max:
        max=i
res=lst3.index(max)
print("the maximum number of the student is:",max)
print("the name of the student is:",lst1[res])
print("the roll number of the student is:",lst2[res])  
