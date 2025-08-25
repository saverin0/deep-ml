def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    m,n = len(a), len(a[0])
    
    b = [[a[i][j] for i in range(m)] for j in range(n)]
    
	return b