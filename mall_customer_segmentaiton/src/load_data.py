# Modules
import pandas as pd
import numpy as np

# Load the data
def load_dataset(filepath):
    """
    Load the xmls data into a 3D Matrix

    Parameter:
    filepath(str): The location of the dataset

    Returns:
    data: A list of 3D matrix. I.e x_i = [(Age, Income, Spending)]
    """
    # Load the data
    data = pd.read_excel(filepath)

    # Get the features
    features = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

    # Convert to matrix
    X = data[features].to_numpy()

    return X


    