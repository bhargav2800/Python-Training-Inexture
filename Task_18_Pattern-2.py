def Pattern(n,center_size):
	temp = ""

	for i in range(n):
		temp += f"{i+1} ".center(center_size," ")
		print(temp)

n = input("Enter the no of rows : ")
if n.isnumeric():
	center_size = 1
	if int(n) > 9 and int(n) < 100:
		center_size = 3
	if int(n) > 99 :
		center_size = 4

	Pattern(int(n),center_size)
else:
	print("Please Enter Valid No of rows !")