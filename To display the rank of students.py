num=int(input("enter how many number do you want in list:"))
lst1=[]
for i in range(num):
    name=input("enter the name:")
    roll=int(input("enter the roll number:"))
    marks=int(input("enter the marks:"))
    lst1.append({"name":name,"rollno":roll,"marks":marks})
print(lst1)
max1=0
max2=None
for i in lst1:
    if i["marks"]>max1:
        max2=i
print("the name of the student is:",max2["name"])
print("the roll number of the student is:",max2["rollno"])
print("the maximum number of the student is:",max2["marks"])
def calc(lst1):
    return lst1["marks"]
lst1=sorted(lst1,key=calc,reverse=True)
rank=1
for i in lst1:
    i["rank"]=rank
    rank+=1
lst1=sorted(lst1,key=lambda x:x["rank"])
print(lst1)
for i in lst1:
    print("name",i["name"])
    print("roll no",i["rollno"])
    print("marks",i["marks"])
    print("rank",i["rank"])
            
        
        
        


