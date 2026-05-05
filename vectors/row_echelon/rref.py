import numpy as np

# Data

house_data = np.array([
    [1000, 2],
    [2000, 4]
])

# Target
target = np.array([200, 400])

# Get the rank

rank = np.linalg.matrix_rank(house_data)

print(rank)

# Solution
sol = np.linalg.solve(house_data, target)
print(sol)