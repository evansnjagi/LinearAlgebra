# Imports
from load_data import load_dataset
from plane import Plane

def run_classifier():
    # Load data
    data = load_dataset("data/Mall_Customers.csv")

    # Define a plane
    plane = Plane(1, -1, 1, -50)

    # Classify the points
    results = []
    for point in data:
        result = plane.classify(point)
        results.append((point, result))
    # Return results
    return results

# Printing the first 10 results
if __name__ == "__main__":
    output = run_classifier()
    for point,result in output[:10]:
        print(point, "->", result)