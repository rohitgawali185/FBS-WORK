def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse


num = int(input("Enter number: "))

print("Reverse =", reverse_number(num))