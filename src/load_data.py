# Imports
import csv

# Loading function
def load_dataset(filepath):
    data = []

    # Open the csv file in dict format
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)

        # Get data features
        for row in reader:
            x = int(row["Age"])
            y = int(row["Annual Income (k$)"])
            z = int(row["Spending Score (1-100)"])

            # Append a tuple to data
            data.append((x, y, z))
    return data

# Testing
if __name__ == "__main__":
    filepath = "data/Mall_Customers.csv"
    data = load_dataset(filepath)
    
    # Print the first 5 rows
    for point in data[:5]:
        print(point)