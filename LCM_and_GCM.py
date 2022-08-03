# Function to compute LCM
def compute_lcm(num1, num2):
    i = 2
    factor1 = []
    factor2 = []
    temp1 = 0
    temp2 = 0
    factor = 1
    while True:
        temp = 0
        if (num1 % i) == 0 and temp1==0:
            factor1 += [i]
            num1 //= i
            temp = 1
            if num1 == 1:
                temp1 = 1
        if (num2 % i) == 0 and temp2==0:
            factor2 += [i]
            num2 //= i
            temp = 1
            if num2 == 1:
                temp2 = 1
        
        if num1 == 1 and temp1==0:
            factor1 += [num1]
            temp1=1

        if num2 == 1 and temp2==0:
            factor2 += [num1]
            temp2=1           


        if temp == 0:
            i = i + 1

        if temp1==temp2==1:
            break
            
    for i in factor1:
        if i in factor2:
            factor2.remove(i)

    factor1 = factor1 + factor2

    for j in factor1:
        factor *= j

    return factor



# FUnction to compute GCM
def compute_gcm(num1, num2):
    if num1 == 0:
        return num2
    return compute_gcm(num2 % num1, num1)



#Main Program
n = input("Enter The number of elements : ")
if n.isnumeric():   
    l = []
    i = 0
    while i< int(n):
        number = input(f"Enter the element {i+1} : ")
        if number.isnumeric():
            l += [int(number)]
            i+=1
        else:
            print("Please Enter Valid Input")

    print(l)

    if int(n) >1:
        temp =0
        # GCM,LCM Function Calling
        gcm = compute_gcm(l[0],l[1])
        j = 2
        while j<len(l):
            gcm = compute_gcm(gcm, l[j])
            j+=1

        print("The G.C.M. is : ", gcm)

        if 0 in l:
            lcm = 0
            temp = 1
        if temp==0:
            lcm = compute_lcm(l[0],l[1])

        j = 2
        while j<len(l):
            if temp==0:
                lcm = compute_lcm(lcm, l[j])
            j+=1

        print("The L.C.M. is : ", lcm)
        
    else:
        print(f"There is only one element so lcm & gcm = {l[0]}")

else:
    print("Please Enter Valid Input !")
