lst=int(input("enter how many number do you want in list:"))
lst1=[]
for i in range(lst):
    num=input("enter the string:")
    lst1.append(num)
print("the list generated is:",lst1)
for i in range(0,len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i]<=lst1[j]:
            lst1[i],lst1[j]=lst1[j],lst1[i]
print("the sorted list is:",lst1)
