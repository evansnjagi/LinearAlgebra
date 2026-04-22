# Modules
from src.get_data import Getdata

rp = Getdata()

df = rp.get_dataframe()

print("DataFrame shape: ", df.shape)
print("\nInfo: ")
print(df.info())
print("\n Top 5 houses: ")
print(df.head())

# Get augmented data
feature1 = "LotFrontage"
feature2 = "LotArea"
aug_matrix = rp.get_augmented_matrix(feature1, feature2)

print("\n Augmented Matrix: ")
print(aug_matrix)