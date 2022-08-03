def rearrange(arr, n):
    for i in range(n):
    	# logic : Dividend = Quotient * Divisor + Reminder
    	# Dividend % Divisor = Reminder
        arr[arr[i]%n] += i*n
    # print(arr)
    for i in range(n):
		# Diviend / divisor = Quotient
        arr[i] //= n

    print("Re-arranged array is :",arr)

# Main code
n = input("Enter The number of elements : ")
if n.isnumeric():
    arr = []
    i = 0 
    while i<int(n):
        el = input(f"Enter the element for position-{i} : ")
        if el.isnumeric():
            if int(el)<int(n):
                arr += [int(el)]
                i+=1
            else:
                print(f"Please Enter element Between 0 - {int(n)-1}")
        else:
            print("Please enter valid input")
    
    if len(arr) == len(set(arr)):
        print("Given array is       :",arr)
        rearrange(arr, int(n))
    else:
        print("Re-arrangement Not Possible! Please enter Unique Values Only!")
else:
    print("Please Enter Valid Input !")
