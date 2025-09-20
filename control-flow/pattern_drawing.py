
# pattern_drawing.

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

row = 0  # row counter

# Outer loop (rows)
while row < size:
    # Inner loop (columns) prints stars side by side
    for col in range(size):
        print("*", end="")  # stay on the same line
    print()  # move to the next line after a row is complete
    row += 1
