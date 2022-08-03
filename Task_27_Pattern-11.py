# Information : 
# m - rows
# k - point to rows
# n = column
# l - point to column

#Function for filling the matrix in circular manner
def Pattern(m,n,matrix):
    k, l = 0, 0
    counter = 1

    while k<m and l<n:
        # first row from the remaining rows.
        i = l
        while i<n:
            matrix[k][i] = counter
            counter+=1
            i+=1
        k+=1

        # last column from the remaining columns.
        i=k
        while i<m:
            matrix[i][n-1] = counter
            counter+=1
            i+=1
        n-=1

        # last row from the remaining rows.
        if k<m:
            i=n-1
            while i>l-1:
                matrix[m-1][i] = counter
                counter+=1
                i-=1
            m-=1

        # first column from the remaining columns.
        if l<n:
            i=m-1
            while i>k-1:
                matrix[i][l] = counter
                counter+=1
                i-=1
            l+=1

    return matrix



# Main Body
while True:
    print("Chose Your Sprial Pattern Type : ")
    print("1. N*N")
    print("2. N*M")

    option = input("Please Enter Your choice [1,2] : ")

    if option == '1':
        m = input("Enter the no of rows for spiral pattern : ")
        n=m
        break
    elif option == '2':
        m = input("Enter the no of rows : ")
        n = input("Enter the no of Columns : ")
        break
    else:
        print("Please Chose Valid Option")

if m.isnumeric() and n.isnumeric() and int(m)>0 and int(n)>0:

    matrix = [[0 for j in range(int(n))] for i in range(int(m))]

    #Function Calling for filling the matrix
    matrixfill = Pattern(int(m),int(n),matrix)

    center_size = 1
    if int(n)*int(m) > 9 and int(n)*int(m) < 100:
        center_size = 2
    elif int(n)*int(m) > 99 and int(n)*int(m) < 1000:
        center_size = 3

    elif int(n)*int(m) > 999 :
        center_size = 4

    # Print the matrix
    for i in range(int(m)):
        for j in range(int(n)):
            print(str(matrixfill[i][j]).center(center_size," "),end=" ")
        print()
else:
    print("Please Enter Valid Input For Row and Columns !")