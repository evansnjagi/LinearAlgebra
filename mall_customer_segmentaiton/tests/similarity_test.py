# Modules
from src.similarity_analysis import customer_similarity_analysis
from src.load_data import load_dataset

# data
filepath = "data/Mall Customers.xlsx"

X = load_dataset(filepath)

# Distance analysis for the first five customers
for i in range(5):
    for j in range(i + 1, 5):
        d = customer_similarity_analysis(X[i], X[j])
        print(f"Customer {i + 1} Vs. Customer {j + 1} Distance: {d:.2f}")