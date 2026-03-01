import sys

num = int(input("Enter the number: "))
sum = 0
if num<0:
    print("invalid choice")
    sys.exit()
    
for i in range(1, num+1):
    sum = sum + i
    
print("The sum =", sum)
