# Modules
import numpy as np

from src.load_data import load_dataset

# Get the matrix 
filepath = "data/Mall Customers.xlsx"

X = load_dataset(filepath)

# Similarity analysis function
def customer_similarity_analysis(customer_1, customer_2):
    """
    compute the euclidean distance between two customers

    Parameters
    customer_1(int): Customer index(integer between 1 -200)
    customer_2(int): Second customer index(must be an integer)

    Returns:
    distance(float): The similarity distance between the two vectors
    """
    return np.linalg.norm(X[customer_2] - X[customer_1])

