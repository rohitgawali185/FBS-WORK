def strong(n):
    temp = n
    total = 0

    while n > 0:
        digit = n % 10

        fact = 1
        for i in range(1, digit + 1):
            fact = fact * i

        total = total + fact
        n = n // 10

    if temp == total:
        return True
    else:
        return False

n = int(input("Enter number: "))
print(strong(n))