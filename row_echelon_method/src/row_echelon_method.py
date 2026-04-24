# Row Echelon Method algorithm
class RowEchelon:
    def __init__(self):
        "Class inistantiation"
    def get_row_echelon(self, aug_matrix):
        """
        Compute the row echelon reduction solutions.

        Parameter:
        aug_matrix(np.array(3* n)): Augmented matrix

        Return:
        System solution.
        """
        m = aug_matrix.astype(float).copy()


        # Get the rows and columns
        rows, cols = m.shape

        # Instantiate pivot row
        pivot_row = 0

        for col in range(cols - 1):
            for i in range(pivot_row, rows):
                if m[i, col] != 0:
                    print(m[[pivot_row, i]])