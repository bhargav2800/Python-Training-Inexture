def Pattern(n,center_size):
	counter=1
	i=0
	while i<n:
		j=0
		while j<i+1:
			print(str(counter).center(center_size," "),end=" ")
			counter+=1
			j+=1
		print()
		i+=1

n = input("Enter the no of rows : ")
if n.isnumeric():
	center_size = 1
	if int(n) > 4 and int(n)<14:
		center_size = 2
	elif int(n) > 13:
		center_size = 4
	Pattern(int(n),center_size)
else:
	print("Please Enter Valid No of rows !")