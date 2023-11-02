ch="yes"
while ch=="yes":
    num=int(input("enter the number in the range of 1-10:"))
    if num>=1 and num<=2:
        print("########## 52.00%")
    elif num>=3 and num<=4:
        print("###### 28.00%")
    elif num>=5 and num<=6:
        print("# 4.00%")
    elif num>=7 and num<=8:
        print("0.00%")
    else:
        print("### 16%")
    ch=input("do you want to continue(yes/-1)?:")
    
