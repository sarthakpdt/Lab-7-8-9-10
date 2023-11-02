lst=int(input("enter how many number do you want in list:"))
lst1=[]
for i in range(lst):
    num=input("enter the string:")
    lst1.append(num)
print("the list generated is:",lst1)
for j in lst1:
    if j.islower():
        j=j.upper()
    lst1.append(j)
print(lst1)
    
