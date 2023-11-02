R1=2
C1=2
matrix1=[] 
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
    for j in range(i+1,C1):
        if matrix1[i][j]!=0:
            print("the matrix is a upper triangular matrix")
        else:
            print("the matrix is not a upper triangular matrix")
for i in range(R1):
    for j in range(0,i):
        if matrix1[i][j]!=0:
            print("the matrix is a lower triangular matrix")
        else:
            print("the matrix is not a lower triangular matrix")
