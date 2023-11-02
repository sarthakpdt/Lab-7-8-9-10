lst=int(input("enter how many number do you want in list:"))
lst1=[]
sum=0
pr=1
max=lst1[0]
for i in range(lst):
    num=input("enter the string:")
    lst1.append(num)
print("the list generated is:",lst1)
for i in lst1:
    sum+=i
    pr*=i
    if i>max:
        max=i
print("the sum of all the number is:",sum)
print("the product of all the number is:",pr)
print("the maximum number from all number is:",max)
