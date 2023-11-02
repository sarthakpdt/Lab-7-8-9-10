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
union=res1.union(res2)
intersection=res1.intersection(res2)
difference1=res1.difference(res2)
difference2=res2.difference(res1)
symmetric_difference=difference1.union(difference2)
print("Union of sets A and B:",union)
print("Intersection of sets A and B:",intersection)
print("Set difference A - B:",difference1)
print("Set difference B - A:",difference2)
print("Symmetric Set Difference:",symmetric_difference)


