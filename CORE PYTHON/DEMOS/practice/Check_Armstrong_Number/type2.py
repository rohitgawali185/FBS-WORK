def armstrong(n):
    temp = n
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n = n // 10

    if temp == total:
        print(True)
    else:
        print(False)

n = int(input("Enter number: "))
armstrong(n)