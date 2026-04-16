# Modules
from src.customer_recommender import find_similar_customers
from src.load_data import load_dataset

filepath  = "data/Mall Customers.xlsx"

X = load_dataset(filepath)

# Compute similarity cosine
similar_customers = find_similar_customers(X)

print(similar_customers)
