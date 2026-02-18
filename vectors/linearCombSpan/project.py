# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define vectors
v1 = np.array([1,1]) # Try vector [1, 0] and only this vector
v2 = np.array([1, -1]) # Try vector [0, 1] and only this vector

# Generate linear combinations

points = []

# Setting weights at an interval [-5, 5]
a_weight = np.linspace(-5, 5, 20)
b_weight = np.linspace(-5, 5, 20)

# Populating the points
for i in a_weight:
    for j in b_weight:
        point = (v1 * i) + (v2 * j)
        points.append(point)

# Setting points back to a vector
points = np.array(points)

# Plot the span
plt.scatter(points[:, 0], points[:, 1])
plt.axvline(0)
plt.axhline(0)
plt.gca().set_aspect("equal")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Span of v1 and v2")
plt.grid(True)
plt.savefig("span_of_v1_and_v2.png")