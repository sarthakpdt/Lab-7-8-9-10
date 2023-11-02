num=int(input("enter the number of elements you want to enter in the first list:"))
lst1=[]
for i in range(num):
    num1=int(input("enter the number:"))
    lst1.append(num1)
print("the first list is:",lst1)
num2=int(input("enter the number of elements you want to enter in the second list:"))
lst2=[]
for j in range(num2):
    num3=int(input("enter the number:"))
    lst2.append(num3)
print("the second list is:",lst2)
print("the first list converted to set is:",set(lst1))
print("the second list converted to set is:",set(lst2))
