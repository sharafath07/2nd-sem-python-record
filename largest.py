num1, num2 = map(int, input("Enter two numbers: ").split())

if num1>num2:
    print(num1, " is the Largest")
elif num1<num2:
    print(num2, " is the Largest")
else:
    print("The numbers are Equal")
