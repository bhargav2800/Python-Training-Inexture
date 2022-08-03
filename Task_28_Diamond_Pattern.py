# Diamond Pattern Function
def Pattern(n):
	i=0
	j=0
	while i<(int(n)*2):
		if i<n:
			print('  '*(int(n)-i-1),end="")
			print('* '*((int(i+1)*2) -1))
		else:
			print('  '*(j+1),end="")
			print('* '*(((int(n-1)-j) * 2)-1))
			j+=1
			pass
		i+=1

n = input("Enter the no of rows : ")
if n.isnumeric():
	Pattern(int(n))
else:
	print("Please Enter Valid No of rows !")