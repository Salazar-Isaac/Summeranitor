# Sample data with two columns: values and units
data = [
    (6, 'dm'),
    (4, 'dm'),
    (30, 'cm'),
    (600, 'mm'),
    (1, 'dm'),
    (40, 'cm'),
    (50, 'mm'),
    (50, 'cm'),
    (10, 'cm'),
    (5, 'dm'),
    (60, 'cm'),
    (7, 'dm'),
    (2, 'dm'),
    (90, 'cm'),
    (500, 'mm'),
    (10, 'cm'),
    (300, 'mm'),
    (40, 'cm'),
    (8, 'dm'),
    (400, 'mm'),
    (800, 'mm'),
    (10, 'cm'),
    (1, 'dm'),
    (4, 'dm'),
    (400, 'mm'),
    (100, 'mm'),
    (10, 'cm'),
    (40, 'cm'),
    (6, 'dm'),
    (8, 'dm'),
    (500, 'mm'),
    (60, 'cm'),
    (150, 'mm'),
    (1, 'dm'),
    (300, 'mm'),
    (42, 'cm'),
    (4, 'dm'),
    (18, 'cm'),
    (40, 'cm'),
    (80, 'cm'),
    (40, 'cm'),
    (5, 'dm'),
    (2, 'dm'),
    (800, 'mm'),
    (200, 'mm'),
    (30, 'cm'),
    (3, 'dm'),
    (150, 'mm'),
    (20, 'cm'),
    (4, 'dm'),
    (350, 'mm'),
    (10, 'cm'),
    (7, 'dm'),
    (20, 'cm'),
    (1, 'dm'),
    (50, 'mm'),
]

# Define unit conversion factors
conversion_factors = {
    'm': 100,      # Meters (already in meters)
    'mm': 0.1,   # Millimeters to meters
    'dm': 10,     # Decimeters to meters
    'cm': 1,    # Centimeters to meters

}

# Create a new 8x8 grid for the converted values
grid = [[' ' for _ in range(8)] for _ in range(8)]

# Convert units to meters and place them in the grid
for i in range(8):
    for j in range(8):
        if i * 8 + j < len(data):
            value, unit = data[i * 8 + j]
            if unit in conversion_factors:
                converted_value = value * conversion_factors[unit]
                grid[i][j] = f'{converted_value:.2f} cm'

# Print the 8x8 grid
for row in grid:
    print('|'.join(row))