# Optimized Code
# Complexity : approx : O(sqrt(n))    --->>>  loop will execute sqrt(n) or sqrt(n)+1  times

def Factor(n):
	i = 1
	l = []
	while True:
		if (n % i == 0):
			if (n / i == i) :
				l+=[i]
				break
			else :
				if i*i > n:
					break
				else:
					l+=[i]
					l+=[int(n/i)]
		i = i + 1
	print(sorted(l))

number = input("Enter the number : ")

if number.isalpha():
	print("Please Enter Integer Values !")
else:
	if number.isdigit() or number[1:].isdigit():
		if int(number)>0:
			Factor(int(number))
		elif int(number)<0:
			Factor(abs(int(number)))
		else:
			print("All Numbers are Factore of Zero")
	else:
		print("Please Enter Integer Values !")

	