# Enqueue Function to Push item into the Circular Queue
def q_enqueue(q,item, front, rear):
	if ((front==0 and rear==qsize-1) or (front == rear+1)):
		print("Queue is full (Overflow) !")
		return front,rear

	else:
		if(front == -1 & rear == -1):
			front = 0
			rear = 0
			q[rear] = item
			print(f"{item} added successfully in Queue")
			return front,rear

		else:
			rear = (rear+1)%qsize
			q[rear] = item
			print(f"{item} added successfully in Queue")
			return front,rear



# Dequeue Function to Pop item into the Circular Queue
def q_dequeue(q, front, rear):
	if front == -1 and rear == -1:
		print("Queue is Empty (UnderFlow !)")
		return -1,-1

	else:
		if front == rear:
			temp = q[front]
			q[front] = ""
			print(f"{temp} is Popped successfully from Queue")
			return -1,-1
		else:
			temp = q[front]
			q[front] = ""
			print(f"{temp} is Popped successfully from Queue")
			front = (front + 1) % qsize
			return front,rear		

		

# Display function to see the Circular Queue condition
def q_display(q, front, rear):
	if(front == -1 & rear == -1):
		print("Queue is Empty (UnderFlow !)")
	else:
		i = 0
		while i<qsize:
			if i==front and i==rear:
				print(f"{q[i]}  <<-- Front & Rear")
			elif i == front:
				print(f"{q[i]}  <<--  Front")
			elif i == rear:
				print(f"{q[i]}  <<--  Rear")
			else:
				if q[i] == "":
					print("Empty")
				else:
					print(q[i])
			i+=1


# variable Decleration
Front = -1
Rear  = -1
qsize = int(input('Please Enter the size of Circular queue : '))
Q = [""]*qsize
# Loop For provide options to user (Body)
while True:
	if qsize <= 0:
		print("Size of Queue should be greater then 0")
		qsize = int(input('Please Enter the size of queue : '))
	else:
		print("Please chose function that you want to perform onn stack: ")
		print("(1) Enqueue")
		print("(2) Dequeue")
		print("(3) Display")
		print("(4) Exit")

		choice = input('Enter your choice between [1-5] : ')


		if(choice=='1'):
			i = int(input('Please Enter the Number you want to push :'))
			Front,Rear = q_enqueue(Q,i,Front,Rear)

		elif(choice=='2'):
			Front,Rear = q_dequeue(Q,Front,Rear)

		elif(choice=='3'):
			q_display(Q,Front,Rear)

		elif(choice=='4'):
			print("Exit successfully")
			break

		else:
			print("Please Enter valide Choice between [1-5]")