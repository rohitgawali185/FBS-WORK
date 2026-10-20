def remove_nth_index(s, n):
    if n < 0 or n >= len(s):
        return "Invalid index"
    return s[:n] + s[n+1:]

text = "FirstBit"
print("After removal:", remove_nth_index(text, 3))