R1=int(input("enter the number of rows for first matrix:"))
C1=int(input("enter the number of colomns for first matrix:"))
matrix1=[] 
for i in range(R1): 
    row=[] 
    for j in range(C1): 
        x=int(input("enter the number for first matrix:")) 
        row.append(x) 
    matrix1.append(row) 
R2=int(input("enter the number of rows for second matrix:"))
C2=int(input("enter the number of colomns for second matrix:"))
matrix2=[] 
for i in range(R2): 
    row=[] 
    for j in range(C2): 
        x=int(input("enter the number for second matrix:")) 
        row.append(x) 
    matrix2.append(row)
mul_matrix=[]
if C1==R2:
    for i in range(len(matrix1)): 
        row=[] 
        for j in range(len(matrix2[0])): 
            element=0
            for k in range(len(matrix2)):
                element+=matrix1[i][k]*matrix2[k][j]
            row.append(element) 
        mul_matrix.append(row) 
else:
    print("matrix cannot be multiplied")
print("first matrix:")
for i in matrix1: 
    print(i)  
print("second matrix:")
for i in matrix2: 
    print(i)  
print("the multiplication of 2 matrix is:")
for i in mul_matrix:
    print(i)

