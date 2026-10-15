def fibonacci(n):
    if n <= 0:
        return
    else:
        print(a, end=" ")
        next_num = a + b
        globals()["a"] = b
        globals()["b"] = next_num
        fibonacci(n - 1)


a = 0
b = 1

n = int(input("Enter number of terms: "))

fibonacci(n)