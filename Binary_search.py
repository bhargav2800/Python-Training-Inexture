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



# Binary Search Algo
def binary_Search(lst,key,l,u):

	while l<=u:

		mid = (l + u)//2

		if lst[mid] == key:
			return True,mid


		elif key > lst[mid]:
			l = mid + 1

		elif key < lst[mid]:
			u = mid - 1
				

	return False,None
			






# Define a Static list
lsize = int(input('Please Enter the size of list : '))
if lsize <= 0:
		print("Size of list should be greater then 0")
else:
	num = []
	i=0
	while i < lsize :
		num += [int(input(f"Please Enter the element at Position {i+1} : "))]
		i+=1

	#Take a input from user to search for perticular key
	key = int(input("Please Enter the key that you want to search :"))

	l = 0
	u = lsize - 1

	# Creating a object of Class


	# sort function calling
	sort(num,lsize)
	print("Sorted list : ",num)
	# Calling Function
	flag,index = binary_Search(num,key,l,u)


	# Print Result
	if flag:
		print(f"key : {key} Found at Position: {index+1}")

	else:
		print("Provided key does not exists !..")

