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
    for j in range(C1):
        if matrix1[i][j]==matrix1[j][i]:
            print("the matrix is symmetrics")            
        else:
            print("the matrix is not symmetrics")
