def Pattern(n,center_size):
	i=n
	while i>=0:
		j=0
		while j<i:
			print(str(j+1).center(center_size," "), end=" ")
			j+=1
		print()
		i-=1	

n = input("Enter the no of rows : ")
if n.isnumeric():
	center_size = 1
	if int(n) > 9:
		center_size = 3
	Pattern(int(n),center_size)
else:
	print("Please Enter Valid No of rows !")