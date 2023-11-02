def sum(num):
    if num<0:
        return "wrong number"
    elif num==0 and num==1:
        return 1
    else:
        return num+sum(num-1)
num=int(input("enter the number:"))
print(sum(num))
    
