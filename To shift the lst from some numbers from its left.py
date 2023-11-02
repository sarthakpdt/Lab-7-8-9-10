def calc(lst,num):
    a=lst.index(num)
    b=lst[:a]
    lst.append(b)
    for i in b:
        lst.remove(i)
    return lst
lst=eval(input("enter the list:"))
num=int(input("enter the number:"))
print(calc(lst,num))
