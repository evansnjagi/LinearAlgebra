# Test
from src.mat_vect import mat_vect_mult
A = [[2, 1], [0, 3]]
x = [4, 5]

# Transformation
print(f"\nTransforming {x}")
transformation = mat_vect_mult(A, x)

# Transforming e1
e1 = [1, 0]

print(f"\nTransforming {e1}")
result = mat_vect_mult(A, e1)

# Transforming e2
e2 = [0, 1]

print(f"\nTransforming: {e2}")
result2 = mat_vect_mult(A, e2)