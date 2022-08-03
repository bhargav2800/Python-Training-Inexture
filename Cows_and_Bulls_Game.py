def Guessing(generated_number, count_cow, count_bull):
	
	count_guessing = 0

	while True:
		num = input("Please Enter 4 digit number that you want to try: ")
		if num.isnumeric():
			dic = {}
			j=1
			for i in generated_number:
				dic[j] = i
				j+=1

			count_guessing += 1
			cow = 0
			bull = 0

			if (len(num) == 4):

				if(num == generated_number):
					return count_cow,count_bull,count_guessing

				else:
					print("Opps! You guessed it wrong!")
					temp = []
					lst = []
					j=1
					for i in num:
						if i == dic[j]:
							cow+=1
							dic.pop(j)
						else:
							temp += i
							lst += dic[j]
						j+=1

					for i in temp:
						if i in lst:
							bull+=1
							lst.remove(i)

					print(f"{cow} cow , {bull} bull")
					count_cow  += cow
					count_bull += bull

			else:
				print("Please Enter Valide input")

		else:
			print("Please Enter Valide Input")
			


# Generate Random number of 4 digit
import random
# str(random.randint(1000,9999))
generated_number = "3116"

# print(generated_number)

count_cow = 0
count_bull = 0

#Gussing_number function calling
count_cow,count_bull,count_guessing = Guessing(generated_number, count_cow ,count_bull)

print(f"Yeah! You guessed it right in {count_guessing} tries.")
print(f"You have total {count_cow} cows & {count_bull} bulls")