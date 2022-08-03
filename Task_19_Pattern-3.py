def Pattern(n):
	temp = ""
	for i in range(n):
		print((chr(i+65)+" ") * (i+1))


n = input("Enter the no of rows : ")
if n.isnumeric() and int(n)<27:
	Pattern(int(n))
else:
	print("Please Enter Valid No of rows !")