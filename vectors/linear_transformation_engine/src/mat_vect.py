def mat_vect_mult(A, x):
    """
    Multiply a matrix A by a vector x.

    Parameters:
        A(list of list): Matrix (m x n)
        x(list): Vector(n, 1)

    Returns:
        list: Result vector(m, 1)
    """
    # Step 1. Dimension check
    if len(A[0]) != len(x):
        raise ValueError("Dimension mismatch!")

    result = []

    for i, row in enumerate(A):

        total = 0
        steps = []
        
        for j in range(len(x)):
            product = row[j] * x[j]
            total += product
            steps.append(f"{row[j]} * {x[j]}")
        
        # Print results output
        print(f"Row {i + 1}: {' + '.join(steps)} = {total}")
        result.append(total)
    
    print(f"\nInput vector: {x}")
    print(f"Output vector: {result}")
    print("Transformation complete.\n")

    return result