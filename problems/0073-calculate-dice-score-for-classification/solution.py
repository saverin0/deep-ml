
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	fn = np.sum((y_true == 1) & (y_pred == 0))
	bottom = 2 * tp + fp + fn
	res = 2 * tp / (bottom)
	return round(res if bottom != 0 else 0.0, 3)
