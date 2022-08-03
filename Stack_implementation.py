# Push Function to Push item into the stack
def s_push(stack,item,Top,qsize):
	if Top+2 <= qsize:
		stack += [item]
		print(f"{item} added successfully in Stack")
		return Top + 1,stack
	else:
		print("Stack is full (Overflow) !")
		return Top,stack


# Pop Function to Pop item into the stack
def s_pop(stack,Top):
	if(Top == -1):
		print("Stack is Empty (UnderFlow!)")
		return Top,stack
	else:
		temp = stack[Top]
		print(f"{temp} is Popped successfully from Stack")
		return Top - 1,stack[:-1]



# Peek Function to see the Top item in the stack
def s_peek(stack,Top):
	if(Top == -1):
		print("Stack is Empty (UnderFlow!)")

	else:
		print(stack[Top])


# Display function to see the stack condition
def s_display(stack,Top):
	if(Top == -1):
		print("Stack is Empty (UnderFlow!)")
	
	else:
		print(f"{stack[Top]}  <<-- Top")
		i = Top-1
		while i >= 0:
			print(stack[i])
			i-=1



# Loop For provide options to user (Body)
# variable Decleration
S = []
qsize = int(input('Please Enter the size of Stack: '))
Top = -1
while True:
	if qsize <= 0:
		print("Size of Stack should be greater then 0")
		qsize = int(input('Please Enter the size of Stack : '))
	else:
		print("Please chose function that you want to perform onn stack: ")
		print("(1) Push")
		print("(2) Pop")
		print("(3) Peek")
		print("(4) Display")
		print("(5) Exit")

		choice = input('Enter your choice between [1-5] : ')

		if(choice=='1'):
			i = int(input('Please Enter the Number you want to push :'))
			Top,S = s_push(S,i,Top,qsize)


		elif(choice=='2'):
			Top,S = s_pop(S,Top)

		elif(choice=='3'):
			s_peek(S,Top)

		elif(choice=='4'):
			s_display(S,Top)

		elif(choice=='5'):
			print("Exit successfully")
			break

		else:
			print("PLease Enter valide Choice between [1-5]")
