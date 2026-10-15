def armstrong(num):

    original = num
    sum = 0
    digits = len(str(num))

    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10

    if original == sum:
        return True
    else:
        return False


num = int(input("Enter number: "))

if armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")