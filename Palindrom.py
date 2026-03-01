num = int(input("Enter the number: "))
pal = num
rev = 0

while num!=0:
    d = num % 10
    rev = rev * 10 + d
    num = num//10

if rev == pal:
    print("The number is palindrom")
else:
    print("The number is not palindrom (",rev,")")
