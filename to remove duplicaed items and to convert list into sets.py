num=int(input("how many numbers do you want to enter:"))
lst=[]
for i in range(num):
    sen=int(input("enter the number:"))
    lst.append(sen)
print(lst)
res=set(lst)
print(res)
for j in lst:
    if j in res:
        print(j)
        res.remove(j)
    
