def feb(num):
    if num<0:
        return "wrong number"
    else:
        return feb(num-1)+feb(num-2)
num=int(input("enter the number:"))
print(feb(num))
    
