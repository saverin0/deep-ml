import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	data = np.array(vectors)
	table =[]
	for k in range(len(data)):
		row = []
		for j in range(len(data)):
			b_k  = np.average(data[k])
			dev_k = (data[k] - b_k)
			b_j = np.average(data[j]) 
			dev_j = (data[j] - b_j)
			cov = np.sum(dev_k * dev_j).item() / (len(data[0]) - 1)
			row.append(cov)
		table.append(row)
	return table