#function to insert data in two input matrics
def Input_matrics(m,n):
	l = []
	i=0
	while i<m:
		temp = []
		j=0
		while j<n:
			temp += [int(input(f"Please enter a value for position {i} * {j} : "))]
			j+=1
		l+=[temp]
		i+=1
	return l

#Function to find the determinant
def determinant(mat,m):
	if m==2:
		value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
		return value
	else:
		Counter = 1
		deter = 1
		i = 0
		while i<m-1:
			j=i+1
			while j<m:
				# When the value of diagonal is zero makeing that value to nearest of zero
				if mat[i][i] == 0:
					mat[i][i] = 1.0e-18
				
				temp1 = mat[i][i]
				temp2 = mat[j][i]
				k=0
				while k<m:
					mat[j][k] = (temp1*mat[j][k]) - (temp2*mat[i][k])
					k+=1

				Counter *= temp1
				j+=1
			i+=1
		i = 0
		while i<m:
			deter *= mat[i][i]
			i+=1
		return int(deter/Counter)

def size_check(l):
	if l<=0:
		print("Invalid Size of Matrix !")
		print("Note: Size of matrix should be grater then 0")
		exit()
	else:
		return l

#Main body
# for size of matrics
m = size_check(int(input("Please Enter No. of Rows for matrics : ")))
n = size_check(int(input("Please Enter No. of Cols for matrics : ")))

if m!=n:
	print("Matrix should be square matrix !")

else:
	a = Input_matrics(m,n)
	deter = determinant(a,m)

	#Print Determinent value of matrix
	print(f"Diterminent of given matrics : {deter}")
