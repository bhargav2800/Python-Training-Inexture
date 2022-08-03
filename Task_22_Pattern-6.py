def Pattern(n):
	for i in range(int(n)):
		print('  '*(int(n)-i-1),end="")
		print('* '*((int(i+1)*2) -1))

n = input("Enter the no of rows : ")

if n.isnumeric():
	Pattern(int(n))
else:
	print("Please Enter Valid No of rows !")