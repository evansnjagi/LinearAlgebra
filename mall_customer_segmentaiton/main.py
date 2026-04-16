# Modules
import pandas as pd

from src.customer_recommender import find_similar_customers
from src.load_data import load_dataset

# Get the dataframe
filepath = "data/Mall Customers.xlsx"
df = pd.read_excel(filepath)

# Get the Matrix(X)
X = load_dataset(filepath)

# Find similar customers index
similar_customer_indeces= find_similar_customers(X)

# Print results
print(df.iloc[similar_customer_indeces])