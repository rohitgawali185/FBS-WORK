def perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    if total == n:
        print(True)
    else:
        print(False)

n = int(input("Enter number: "))
perfect(n)