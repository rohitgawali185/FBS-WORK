def perfect():
    n = int(input("Enter number: "))
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    if total == n:
        return True
    else:
        return False

print(perfect())