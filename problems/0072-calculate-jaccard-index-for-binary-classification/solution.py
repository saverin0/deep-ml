import numpy as np

def jaccard_index(y_true, y_pred):
	# Write your code here
  top = np.sum((y_true == 1) & (y_pred ==1))
  bottom = np.sum((y_true == 1) | (y_pred ==1))
  if bottom == 0:
    return 0.0
  else:
    result = top / bottom
  return round(result, 3)
