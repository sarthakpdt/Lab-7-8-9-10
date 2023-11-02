R1=2
C1=2
matrix1=[]
sum1=0
sum2=0
for i in range(R1): 
    row=[] 
    for j in range(C1): 
        x=int(input("enter the elements for matrix:")) 
        row.append(x) 
    matrix1.append(row) 
print("matrix formed is:")
for i in matrix1:
    print(i)
for i in range(R1):
        sum1+=matrix1[i][i]
sum2=matrix1[0][1]+matrix1[1][0]
print("the sum of the princple values of the matrix is:",sum1)
print("the sum of the non principle values of the matrix is:",sum2)
        
