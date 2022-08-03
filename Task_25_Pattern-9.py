def Pattern(n,center_size,center_size_space):
	i = 1
	while i<n+1:
		j = i+1
		while j<n+1:
			print(" ".center(center_size_space," "),end="")
			j+=1
		temp=1
		j=1
		while j<i+1:
			print(str(temp).center(center_size," "), end=" ")
			temp = int(temp * (i - j) / j)
			j+=1
		print()
		i+=1

n = input("Enter the no of rows : ")
if n.isnumeric():
	center_size = 1
	center_size_space = 1
	if int(n) > 5 and int(n) < 14:
		center_size_space = 2
		center_size = 3
	elif int(n) > 13 and int(n) < 21:
		center_size_space = 3
		center_size = 5
	elif int(n) > 20 and int(n) < 28:
		center_size_space = 4
		center_size = 7
	elif int(n) > 27 and int(n) < 34:
		center_size_space = 5
		center_size = 9
	elif int(n) > 33:
		center_size_space = 6
		center_size = 11
	Pattern(int(n),center_size,center_size_space)
else:
	print("Please Enter Valid No of rows !")