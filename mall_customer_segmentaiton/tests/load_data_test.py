# Modules
from src.load_data import load_dataset

filepath = "data/Mall Customers.xlsx"

X = load_dataset(filepath)

print("\nTop 5 matrix data: ")
print(X[:5])