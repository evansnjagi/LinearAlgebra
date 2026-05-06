# Test
from src.mat_vect import mat_vect_mult

def test_basic_case():
    A = [[2, 1], [0, 3]]
    x = [4, 5]

    # Transformation
    result = mat_vect_mult(A, x)
    assert result == [13, 15]
