import numpy as np

def compute_tpr_fpr(y_true, y_pred):
    """
    Compute TPR and FPR from true and predicted binary labels.

    Args:
        y_true (array-like): Ground-truth labels (0 or 1).
        y_pred (array-like): Predicted labels (0 or 1).

    Returns:
        tuple: (tpr, fpr) as Python floats.
    """
    # TODO: compute TP, FN, FP, TN then TPR and FPR
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    bottom_tpr = tp + fn
    bottom_fpr = fp + tn
    if bottom_tpr == 0:
        TPR = 0.0
    else:
        TPR = tp / bottom_tpr
    if bottom_fpr == 0:
        FPR = 0.0
    else:
        FPR = fp / bottom_fpr
    return (TPR,FPR)
