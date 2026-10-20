cols = 10

for row in range(10, 0, -1):
    start = (row - 1) * cols + 1
    end = row * cols
    
    # Even rows (from top 10th row down) print left-to-right or right-to-left
    if row % 2 == 0:
        # Numbers go right to left (100 to 91, 80 to 71, etc.)
        line = list(range(end, start - 1, -1))
    else:
        # Numbers go left to right (81 to 90, 61 to 70, etc.)
        line = list(range(start, end + 1))
        
    print("\t".join(f"{num:3d}" for num in line))