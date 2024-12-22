# pattern_drawing.py

# Prompt the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks in the current row
    for i in range(size):
        print("*", end="")
    # Print a newline character after each row
    print()
    row += 1
