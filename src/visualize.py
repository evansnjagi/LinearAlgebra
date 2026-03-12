# Imports
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from load_data import load_dataset
from plane import Plane

def visualize():
    # Get data
    data = load_dataset("data/Mall_Customers.csv")
    plane = Plane(1, -1, 1, -50)
    npl = []
    sp = []
    pp = []
    for point in data:
        result  = plane.classify(point)
        if result == "Normal":
            npl.append(point)
        elif result == "Suspicious":
            sp.append(point)
        else:
            pp.append(point)

    def extract_xyz(point):
        x = [p[0] for p in point]
        y = [p[1] for p in point]
        z = [p[2] for p in point]

        return x, y, z

    x = [p[0] for p in data]
    y = [p[1] for p in data]

    nx, ny, nz = extract_xyz(npl)
    sx, sy, sz = extract_xyz(sp)
    px, py, pz = extract_xyz(pp)

    # Create the mesh grid
    x_range = np.linspace(min(x), max(x), 10)
    y_range = np.linspace(min(y), max(y), 10)

    X, Y = np.meshgrid(x_range, y_range)

    # Define plane
    plane = Plane(1, -1, 1, -50)

    # Compute z from plane equation
    Z = (-plane.a * X -plane.b * Y - plane.d) / plane.c

    # Create 3D figure
    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    # Plot the points
    ax.scatter(sx, sy, sz, color="red", label = "Suspicious")
    ax.scatter(nx, ny, nz, color = "blue", label = "Normal")
    ax.scatter(px, py, pz, color = "pink", label = "On Plane")

    # Plot plane
    ax.plot_surface(X, Y, Z, alpha=0.3)

    # Axis labelling
    ax.set_xlabel("Age")
    ax.set_ylabel("Annual Income")
    ax.set_zlabel("Spending Score")


    plt.savefig("figures/customer_distribution.png")
    print("Figure saved to figure/ as customer_distribution")

if __name__ == "__main__":
    visualize()