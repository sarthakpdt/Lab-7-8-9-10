num=int(input("enter the number of elements you want to enter in the first list:"))
lst1=[]
for i in range(num):
    num1=int(input("enter the number:"))
    lst1.append(num1)
num2=int(input("enter the number of elements you want to enter in the second list:"))
lst2=[]
for j in range(num2):
    num3=int(input("enter the number:"))
    lst2.append(num3)
res1=set(lst1)
res2=set(lst2)
print("the first set is:",res1)
print("the second set is:",res2)
for k in res2:
    if k in res1:
        print(k)
    
