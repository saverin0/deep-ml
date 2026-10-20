from collections import Counter
import numpy as np

def confusion_matrix(data):
	# Implement the function here 
  data = np.array(data)
  y_true,y_pred = data[:,0],data[:,-1]
  tp = np.sum((y_true == 1) & (y_pred == 1)).item()
  tn = np.sum((y_true == 0) & (y_pred == 0)).item()
  fp = np.sum((y_true == 0) & (y_pred == 1)).item()
  fn = np.sum((y_true == 1) & (y_pred == 0)).item()
  return [[tp,fn],[fp,tn]]
  