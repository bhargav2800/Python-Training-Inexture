def Pattern(n):
	for i in range(n):
		print("* "*(n-i))

n = input("Enter the no of rows : ")
if n.isnumeric():
	Pattern(int(n))
else:
	print("Please Enter Valid No of rows !")