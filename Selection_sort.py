# Selection sort algorithm
def sort(num,l):
	i = 0
	while i < l:
		min_index = i
		j=i
		while j < l:
			if num[j] < num[min_index]:
				min_index = j
			j+=1
		temp = num[i]
		num[i] = num[min_index]
		num[min_index] = temp

		i+=1


# Define a Static list
qsize = int(input('Please Enter the size of list : '))
if qsize <= 0:
		print("Size of list should be greater then 0")
else:
	num = []
	i=0
	while i < qsize :
		num += [int(input(f"Please Enter the element at Position {i+1} : "))]
		i+=1

	# sort function calling
	sort(num,qsize)

	#Printing Sorted list
	print("Sorted list : ",num)