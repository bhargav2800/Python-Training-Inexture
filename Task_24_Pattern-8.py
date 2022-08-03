def Pattern(n):
	for i in range(int(n)):
		print('  '*(i),end="")
		print('* '*(((int(n)-i) * 2)-1))

n = input("Enter the no of rows : ")

if n.isnumeric():
	Pattern(int(n))
else:
	print("Please Enter Valid No of rows !")