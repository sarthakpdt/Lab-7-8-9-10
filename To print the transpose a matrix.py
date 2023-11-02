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
transpose=[[0,0],[0,0]]
for i in range(R1):
    for j in range(C1):
        transpose[i][j]=matrix1[j][i]
print("the transpose the matrix is:")
for i in transpose:
    print(i)
