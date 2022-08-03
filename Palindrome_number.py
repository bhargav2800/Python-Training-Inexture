def palindrom(num):
    num = int(num)
    temp = num
    rev=0

    while temp>0:
        le = temp%10
        temp = temp//10
        rev = rev*10+le

    if num==rev:
        print("The number is Palindrome!")
    else:
        print("Not a Palindrome")

num=input("Enter a number:")

if num.isdigit():
    palindrom(int(num))
else:
    print("Please Enter Numeric integer Value !")