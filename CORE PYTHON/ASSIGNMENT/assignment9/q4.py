def sum_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers(n - 1)


n = int(input("Enter n: "))

print("Sum =", sum_numbers(n))