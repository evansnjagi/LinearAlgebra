# Computing unitVector calculation
# Include
import math 

# Get user inputs
vectors = {"mag": [], "theta": []}
for i in range(2):
    mag = float(input(f"Enter magnitude {i + 1}:"))
    theta = float(input(f"Enter theta {i + 1}:"))
    vectors["mag"].append(mag)
    vectors["theta"].append(theta)

# Compute radiant 
r1 = math.radians(vectors["theta"][0])
r2 = math.radians(vectors["theta"][1])

# Calculate Ux and Uy(cartesian components)
def compute_cartesian_components(mag, theta):
    Ux = mag * math.cos(theta)
    Uy = mag * math.sin(theta)
    return Ux, Uy
# Computing R
Ax, Ay = compute_cartesian_components(vectors["mag"][0], r1)
Bx, By = compute_cartesian_components(vectors["mag"][1], r2)

R1 = Ax + Bx
R2 = Ay + By
print(f"Resultant sum: R1: {round(R1,4)} and R2: {round(R2, 4)}")