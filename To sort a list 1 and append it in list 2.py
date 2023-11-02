lst=int(input("enter how many number do you want in list:"))
lst1=[]
for i in range(lst):
    num=input("enter the string:")
    lst1.append(num)
print("the list generated is:",lst1)
lst3=int(input("enter how many number do you want in list:"))
lst2=[]
for i in range(lst3):
    num=input("enter the string:")
    lst2.append(num)
print("the list generated is:",lst2)
for i in range(0,len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i]<=lst1[j]:
            lst1[i],lst1[j]=lst1[j],lst1[i]
print("the sorted list is:",lst1)
lst1.append(lst2)
print("after appending the list becomes:",lst1)
