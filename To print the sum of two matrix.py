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
sum_matrix=[] 
if (R1==R2) and (C1==C2):
    for i in range(R1): 
        row=[] 
        for j in range(C2): 
            sum=(matrix1[i][j]+matrix2[i][j]) 
            row.append(sum) 
        sum_matrix.append(row)
else:
    print("the sum cannot be performed")
print("first matrix:")
for i in matrix1: 
    print(i)  
print("second matrix:")
for i in matrix2: 
    print(i)  
print("the sum of 2 matrix is:")
for i in sum_matrix:
    print(i)


