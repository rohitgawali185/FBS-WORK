for i in range(1, 6):

    for j in range(5 - i):
        print(" ", end=" ")

    print("*", end=" ")

    if i > 1:
        for j in range(2 * i - 3):
            print(" ", end=" ")

        print("*", end=" ")

    print()


for i in range(4, 0, -1):

    for j in range(5 - i):
        print(" ", end=" ")

    print("*", end=" ")

    if i > 1:
        for j in range(2 * i - 3):
            print(" ", end=" ")

        print("*", end=" ")

    print()