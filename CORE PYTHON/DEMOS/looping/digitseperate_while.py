num =472
sum=0
while (num > 0):
    digit = num % 10
    sum += digit
    #print(digit)
    num = num // 10
print(sum)