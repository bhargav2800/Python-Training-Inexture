def Pattern(n,center_size):
	count=1
	i=0
	while i<n:
		j=i+1
		while j<n:
			print(" ".center(center_size," "),end=" ")
			j+=1
		temp = count
		j=0
		while j<i+1:
			print(str(temp).center(center_size," "), end=" ")
			temp += 1
			j+=1
		temp -=1
		j=0
		while j<i:
			temp -= 1
			print(str(temp).center(center_size," "), end=" ")
			j+=1
		print()
		count +=1
		i+=1

n = input("Enter the no of rows : ")
if n.isnumeric():
	center_size = 1
	if int(n) > 5 and int(n) < 50:
		center_size = 2
	elif int(n) >49:
		center_size = 3
	Pattern(int(n),center_size)

else:
	print("Please Enter Valid No of rows !")