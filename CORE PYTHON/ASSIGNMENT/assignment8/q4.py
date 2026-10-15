def odd_sum(n):
    sum = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            sum = sum + i

    return sum


n = int(input("Enter n: "))

print("Sum of Odd Numbers =", odd_sum(n))