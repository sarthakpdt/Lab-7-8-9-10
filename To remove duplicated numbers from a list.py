num=int(input("how many numbers do you want to enter:"))
lst=[]
count=0
for i in range(num):
    sen=int(input("enter the number:"))
    lst.append(sen)
for j in lst:
    if lst.count(j)>1:
        lst.remove(j)
print(lst)

