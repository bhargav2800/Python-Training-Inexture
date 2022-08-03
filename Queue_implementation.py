# Enqueue Function to Push item into the Queue
def q_enqueue(q,item, front, rear):
	if (rear+2 > qsize) or(front>rear):
		print("Queue is full (Overflow) !")
		return front,rear,q
	else:
		q += [item]
		print(f"{item} added successfully in Queue")
		if(front == -1 & rear == -1):
			return front+1,rear+1,q

		else:
			return front,rear+1,q



# Dequeue Function to Pop item into the Queue
def q_dequeue(q, front, rear):
	
	if((front == -1 & rear == -1) or (front>rear)):
		print("Queue is Empty (UnderFlow !)")
		return front,rear,q,qsize

	else:
		temp = q[front]
		q = q[1:]
		print(f"{temp} is Popped successfully from Queue")
		rear = rear - 1
		return front,rear,q,qsize-1


# Peek Function to see the Top item in the Queue
def q_peek(q, front, rear):
	if((front == -1 & rear == -1) or (front>rear)):
		print("Queue is Empty (UnderFlow !)")

	else:
		print(f"{q[rear]}")


# Display function to see the Circular Condition
def q_display(q, front, rear):
	if((front == -1 & rear == -1) or (front > rear)):
		print("Queue is Empty (UnderFlow !)")
	else:
		if(front == rear):
			print(f"{q[front]}  <<--  Front & Rear")
		else:
			print(f"{q[front]}  <<--  Front")
			i = front+1
			while i<rear:
				print(q[i])
				i+=1

			print(f"{q[rear]}  <<--  Rear")





# variable Decleration
Q = []
Front = -1
Rear  = -1
qsize = int(input('Please Enter the size of queue : '))
# Loop For provide options to user (Body)
if qsize <= 0:
		print("Size of Queue should be greater then 0")

else:
	while True:
		print("Please chose function that you want to perform onn stack: ")
		print("(1) Enqueue")
		print("(2) Dequeue")
		print("(3) Peek")
		print("(4) Display")
		print("(5) Exit")

		choice = input('Enter your choice between [1-5] : ')


		if(choice=='1'):
			i = int(input('Please Enter the Number you want to push :'))
			Front,Rear,Q = q_enqueue(Q,i,Front,Rear)

		elif(choice=='2'):
			Front,Rear,Q,qsize = q_dequeue(Q,Front,Rear)

		elif(choice=='3'):
			q_peek(Q,Front,Rear)

		elif(choice=='4'):
			q_display(Q,Front,Rear)

		elif(choice=='5'):
			print("Exit successfully")
			break

		else:
			print("Please Enter valide Choice between [1-5]")