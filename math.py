

matrix = [
    [6, 4, 3, 6, 1, 4, .5, 5],
    [1, 5, 6, 7, 2, 9, 5, 1],
    [3, 4, 8, 4, 8, 1, 1, 4],
    [4, 1, 1, 4, 6, 8, 5, 6],
    [1.5, 1, 3, 4.2, 4, 1.8, 4, 8],
    [4, 5, 2, 8, 2, 3, 3, 1.5],
    [2, 4, 3.5, 1, 7, 2, 1, 5],
    [1, 4, 2, 1, 1, 2, 3, 5]
]

def find_sums(matrix, target_sum):
    rows = len(matrix)
    cols = len(matrix[0])
    sums = []

    # Check horizontally
    for i in range(rows):
        for j in range(cols - 2):
            triplet = matrix[i][j:j+3]
            if sum(triplet) == target_sum:
                sums.append(((i, j), (i, j+2), 'horizontally', triplet))

    # Check vertically
    for i in range(rows - 2):
        for j in range(cols):
            triplet = [matrix[i+k][j] for k in range(3)]
            if sum(triplet) == target_sum:
                sums.append(((i, j), (i+2, j), 'vertically', triplet))

    # Check diagonally (top-left to bottom-right)
    for i in range(rows - 2):
        for j in range(cols - 2):
            triplet = [matrix[i+k][j+k] for k in range(3)]
            if sum(triplet) == target_sum:
                sums.append(((i, j), (i+2, j+2), 'diagonally (top-left to bottom-right)', triplet))

    # Check diagonally (top-right to bottom-left)
    for i in range(rows - 2):
        for j in range(2, cols):
            triplet = [matrix[i+k][j-k] for k in range(3)]
            if sum(triplet) == target_sum:
                sums.append(((i, j), (i+2, j-2), 'diagonally (top-right to bottom-left)', triplet))

    return sums

target_sum = 10
sums = find_sums(matrix, target_sum)

# Create a function to find diagonal sums (bottom-left to top-right)
def find_diagonal_bottom_left(matrix, target_sum):
    rows = len(matrix)
    cols = len(matrix[0])
    sums = []

    for i in range(2, rows):
        for j in range(cols - 2):
            triplet = [matrix[i-k][j+k] for k in range(3)]
            if sum(triplet) == target_sum:
                sums.append(((i, j), (i-2, j+2), 'diagonally (bottom-left to top-right)', triplet))

    return sums

# Find diagonal sums (bottom-left to top-right) and add them to the existing sums
diagonal_sums = find_diagonal_bottom_left(matrix, target_sum)
sums.extend(diagonal_sums)

# Display the results with numbers and positions
if len(sums) == 0:
    print("No sums of three numbers that add up to 10 found.")
else:
    print(f"Found {len(sums)} sums of three numbers that add up to 10 at the following locations:")
    for start, end, direction, triplet in sums:
        print(f"From [{start[0]},{start[1]}] to [{end[0]},{end[1]}] ({direction}): Numbers {triplet} were added.")