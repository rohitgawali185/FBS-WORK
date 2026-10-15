n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print("Student", i)

    total = 0

    for j in range(5):
        marks = int(input("Enter marks: "))
        total = total + marks

    percentage = total / 5
    total_percentage = total_percentage + percentage

    print("Percentage =", percentage)

average = total_percentage / n

print("Average Percentage =", average)