# Modules
from src.get_data import Getdata
from src.row_echelon_method import RowEchelon

# Get augmented data
feature1 = "LotFrontage"
feature2 = "LotArea"
rp = Getdata()
df = rp.get_dataframe()
aug_matrix = rp.get_augmented_matrix(feature1, feature2)

# Row echelom method
rem = RowEchelon().get_row_echelon(aug_matrix)

print(rem)
