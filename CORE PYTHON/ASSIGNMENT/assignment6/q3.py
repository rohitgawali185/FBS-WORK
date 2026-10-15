for i in range(4):

    for j in range(3 - i):
        print(" ", end="")

    for j in range(i + 1):
        if j == 0 or j == i:
            print(1, end=" ")
        elif i == 2:
            print(2, end=" ")
        else:
            print(3, end=" ")

    print()