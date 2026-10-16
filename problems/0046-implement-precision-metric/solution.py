import numpy as np
def precision(y_true, y_pred):
  bottom = np.sum(y_pred == 1)
  if bottom == 0:
    return 0.0
  else:
    return np.sum((y_pred == 1) & (y_pred == y_true)) / bottom
	

