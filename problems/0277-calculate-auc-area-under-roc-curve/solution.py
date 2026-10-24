import numpy as np

def calculate_auc(y_true, y_scores):
  tpr_list = [0.0]
  fpr_list = [0.0]
  total = 0.0
  y_true = np.array(y_true)
  y_scores = np.array(y_scores)
  bottom_tpr = np.sum(y_true == 1)
  bottom_fpr = np.sum(y_true == 0)
  for i in np.unique(y_scores)[::-1]:
    y_pred_x = y_scores >= i
    tp = np.sum((y_true == 1) & y_pred_x) 
    fp = np.sum((y_true == 0) & y_pred_x) 
    tpr = tp /  bottom_tpr if bottom_tpr !=0 else 0.0
    fpr = fp / bottom_fpr if bottom_fpr !=0 else 0.0
    tpr_list.append(float(tpr))
    fpr_list.append(float(fpr))
  for k in range(len(fpr_list) - 1) :
    width = fpr_list [k+1] - fpr_list[k]
    height = (tpr_list [k+1] + tpr_list[k]) / 2
    total += width * height
  return (total)