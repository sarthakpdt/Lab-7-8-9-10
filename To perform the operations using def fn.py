def calc(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    if y!=0:
        div=x/y
        rem=x%y
    exp=x**y
    return add,sub,mul,div,rem,exp
x=int(input("enter the number:"))
y=int(input("enter the number:"))
print(calc(x,y))

