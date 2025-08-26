import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	# Convert to numpy array
	matrix = np.array(a)
	
	# Check if reshape is possible by comparing total elements
	original_size = matrix.size
	new_size = new_shape[0] * new_shape[1]
	
	if original_size != new_size:
		return []
	
	# Reshape and convert back to list
	try:
		reshaped_matrix = matrix.reshape(new_shape).tolist()
		return reshaped_matrix
	except:
		return []