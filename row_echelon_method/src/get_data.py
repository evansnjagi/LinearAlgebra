# Modules
import numpy as np
import pandas as pd

class Getdata:
    def __init__(self, root_path = "data/"):
        "GetData instantiation"
        self.root_path = root_path

    def get_dataframe(self, filename = "data.csv"):
        """
        Convert the `.csv` file into a pandas dataframe

        Paramenter:
        filename(str): The name of the dataset 

        Return
        df(pd.DataFrame)
        """
        # Filepath
        filepath = f"{self.root_path}{filename}"

        # Read the csv file

        df = pd.read_csv(filepath, sep=",")

        # Return df
        self.df = df
        return df
    
    # Represent augmented matrix
    def get_augmented_matrix(self, feature1, feature2, target = "SalePrice"):
        """
        Represent data as an augmented matrix

        Parameters:
        feature1: The first feature to use
        feature2: The final feature for modelling
        target: The target vector (default: SalePrice)

        Return:
        aug_mat(np.array): an nX3 matrix
        """
        # Validation

        if not hasattr(self, "df"):
            raise ValueError("Dataframe not loaded. Call `get_dataframe()` to get the df")
        
        # Column names
        col_names = self.df.columns
        for col in [feature1, feature2, target]:
            if col not in col_names:
                raise ValueError(f"{col} not found! Available columns: {col_names}")
        
        # Extract columns
        a = self.df[feature1].values
        b = self.df[feature2].values
        c = self.df[target].values

        # Augmented matrix
        aug_mat = np.column_stack((a, b, c))

        self.aug_mat = aug_mat

        return aug_mat
