# Insertion sort algorithm
def sort(num,l):
	i = 1
	
	while i < l:
		j = i
		while j > 0:
			if num[j-1] > num[j]:
				temp = num[j]
				num[j] = num[j-1]
				num[j-1] = temp
			j-=1

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