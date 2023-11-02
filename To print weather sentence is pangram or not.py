sen=input("enetr the sentence:")
lst=[]
count=0
for i in range(65,91):
    op=chr(i)
    lst.append(op)
for kj in lst:
    if kj in sen:
        count+=1
if count==26:
    print("the string is pangram")
else:
    print("the string is not pangram")
