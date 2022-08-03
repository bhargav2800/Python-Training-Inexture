#Function for taking input for matrics
def Input_matrics(m,n,flag):
	l = []
	i=0
	while i<m:
		temp = []
		j=0
		while j<n:
			if flag==0:
				temp += [int(input(f"Please enter a value for position {i} * {j} : "))]
			else:
				temp += [0]
			j+=1
		l+=[temp]
		i+=1
	return l

def multiplication(a,b,c,m1,n1,m2,n2):
	i = 0
	while i<m1:
		j = 0
		while j<n2:
			temp = 0
			k=0
			while k<m2:
				c[i][j] += a[i][k] * b[k][j]
				k+=1
			j+=1
		i+=1

def size_check(l):
	if l<=0:
		print("Invalid Size of Matrix !")
		print("Note: Size of matrix should be grater then 0")
		exit()
	else:
		return l

#Main body
# for size of matrics-1
m1 = size_check(int(input("Please Enter No. of Rows for matrics-1 : ")))
n1 = size_check(int(input("Please Enter No. of Cols for matrics-1 : ")))

#for size of matrics-2
m2 = size_check(int(input("Please Enter No. of Rows for matrics-2 : ")))
n2 = size_check(int(input("Please Enter No. of Cols for matrics-2 : ")))

if n1!=m2:
	print("Matrix MUltiplication Not Possible !")
	print("Hint : No. of rows in matrics-1 and No. of cols in matrics-2 should be same")

else:
	print("Enter Values for matrics-1 : ")
	a = Input_matrics(m1,n1,0)
	print("Enter Values for matrics-2 : ")
	b = Input_matrics(m2,n2,0)
	c = Input_matrics(m1,n2,1)

	#multiplication
	multiplication(a,b,c,m1,n1,m2,n2)

	#Print Matrix
	print("Answer : ")
	i = 0
	while i<m1:
		j = 0
		while j<n2:
			print(str(c[i][j]).center(4), end = ' ')
			j+=1
		print()
		i+=1