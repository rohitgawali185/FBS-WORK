def armstrong():
    n = int(input("Enter number: "))
    temp = n
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** 3
        n = n // 10

    if temp == total:
        return True
    else:
        return False

print(armstrong())