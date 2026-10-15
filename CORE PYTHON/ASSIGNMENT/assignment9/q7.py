def digit_sum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + digit_sum(num // 10)


num = int(input("Enter number: "))

print("Sum of Digits =", digit_sum(num))