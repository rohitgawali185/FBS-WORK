def armstrong(num, digits):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return digit ** digits + armstrong(num // 10, digits)


num = int(input("Enter number: "))

digits = len(str(num))

if armstrong(num, digits) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")