def calc(lst,num):
    a=lst.index(num)
    if sen=="left":
        b1=lst[:a]
        lst.append(b1)
        for i in b1:
            lst.remove(i)
    else:
        length=len(lst)
        c=length-a
        b2=lst[:c]
        lst.append(b2)
        for i in b2:
            lst.remove(i)
    return lst
lst=eval(input("enter the list:"))
num=int(input("enter the number:"))
sen=input("do you want to shift from left or right?:")
print(calc(lst,num))
