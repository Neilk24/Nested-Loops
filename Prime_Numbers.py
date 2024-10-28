lower=int(input("Enter your lower range: "))
upper=int(input("Enter your upper range: "))
print("The prime numbers numbers between", lower, "and", upper,"are: ")

for num in range(lower, upper+1):
    if num>1:
        for i in range(2, num):
            if (num%i==0):
                break
        else:
            print(num)