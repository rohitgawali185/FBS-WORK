def reverse(num, rev):
    if num == 0:
        return rev
    else:
        digit = num % 10
        rev = rev * 10 + digit
        return reverse(num // 10, rev)


num = int(input("Enter number: "))

print("Reverse =", reverse(num, 0))