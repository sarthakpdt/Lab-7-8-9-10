lst=int(input("enter how many number do you want in list:"))
lst1=[]
lst2=[]
for i in range(lst):
    num=int(input("enter the number:"))
    lst1.append(num)
print("the list generated is:",lst1)
for j in lst1:
    if j>=10 and j<=20:
        j=j**2
    lst2.append(j)
print(lst2)
