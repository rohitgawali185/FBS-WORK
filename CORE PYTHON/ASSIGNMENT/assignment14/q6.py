numbers = {2, 3, 5, 7, 9, 10}

number_list = list(numbers)
max_product = None
max_pair = None

for j in range(len(number_list)):
    for k in range(j + 1, len(number_list)):
        product = number_list[j] * number_list[k]

        if max_product is None or product > max_product:
            max_product = product
            max_pair = (number_list[j], number_list[k])

print("Numbers:", numbers)
print("Pair with Maximum Product:", max_pair)
print("Maximum Product:", max_product)