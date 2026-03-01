num = int(input("Enter the number: "))

for i in range(2,num//2+1):
    if num%i==0 or num<0:
        print("The number is not prime number")
        break
else:
    print("The number is prime number")
