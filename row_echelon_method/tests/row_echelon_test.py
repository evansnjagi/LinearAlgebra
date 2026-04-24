# Modules
import numpy as np
from src.get_data import Getdata
from src.row_echelon_method import solver

# Get augmented data
feature1 = "LotFrontage"
feature2 = "LotArea"
rp = Getdata()
df = rp.get_dataframe()
aug_matrix = rp.get_augmented_matrix(feature1, feature2)

# Row echelom method
A = aug_matrix[2:, :2]
b = aug_matrix[2:, 2]

solution = solver(A, b)

print("\n Solution")
print()

