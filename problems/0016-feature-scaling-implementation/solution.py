import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	min = np.min(data, axis=0)
	max = np.max(data, axis=0)
	std = np.std(data, axis=0)
	normalized_data = (data - min) / (max - min)
	mean = np.mean(data, axis=0)
	standardized_data = (data - mean) / std
	return standardized_data, normalized_data