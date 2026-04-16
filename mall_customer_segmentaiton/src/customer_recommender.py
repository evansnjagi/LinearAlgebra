# Modules
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

def find_similar_customers(X, customer_index=1, top_n=5):
    """
    Compute similarity cosine between customers

    Parameters:
    X(matrix): (Age, Income, Spending)
    customer_index(int): The customer we want to reference to
    top_n(int): Number of customers we want to compute similarity cosine to
    """
    # Compute similarity cosine
    similarity_matrix = cosine_similarity(X)

    # Scores
    scores = similarity_matrix[customer_index]

    # Sorting
    index_sort = np.argsort(scores)[::-1]

    # Remove the customer index
    index_sorted = [int(i) for i in index_sort if i != customer_index]

    return index_sorted[:top_n]


