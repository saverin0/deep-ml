def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    
    # Check if matrix is empty
    if not a or not a[0]:
        return -1
    
    # Get number of columns in matrix
    num_cols = len(a[0])
    
    # Check if dimensions are compatible
    if num_cols != len(b):
        return -1
    
    # Check if all rows have the same number of columns
    for row in a:
        if len(row) != num_cols:
            return -1
    
    # Compute dot product for each row
    result = []
    for row in a:
        dot_product = sum(row[i] * b[i] for i in range(num_cols))
        result.append(dot_product)
    
    return result