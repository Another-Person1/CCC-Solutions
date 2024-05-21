# Note: This is a partial solution
def calculate_tape_length(columns, row1, row2):
    tape_length = 0
    for col in range(columns):
        if row1[col] == 1:
            # Check the tiles to the left and right of the current tile
            if col == 0 or row1[col-1] == 0:
                tape_length += 1
            if col == columns-1 or row1[col+1] == 0:
                tape_length += 1
            # Check the tile above the current tile
            if row2[col] == 0:
                tape_length += 1
        elif row2[col] == 1:
            # Check the tiles to the left and right of the current tile
            if col == 0 or row2[col-1] == 0:
                tape_length += 1
            if col == columns-1 or row2[col+1] == 0:
                tape_length += 1
            # Check the tile below the current tile
            if row1[col] == 0:
                tape_length += 1
    return tape_length

# Read input from user
columns = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

# Calculate the length of tape needed
tape_length = calculate_tape_length(columns, row1, row2)

# Print the result
print(tape_length)
