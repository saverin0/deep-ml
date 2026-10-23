import numpy as np

def compute_roc_curve(y_true: list, y_scores: list) -> tuple:
    """
    Compute ROC curve points (FPR, TPR) for binary classification.
    
    Args:
        y_true: Binary ground truth labels (0 or 1)
        y_scores: Predicted scores/probabilities for the positive class
    
    Returns:
        Tuple of (fpr, tpr) where each is a list of floats
    """
    # Your code here
    tpr_list = [0.0]
    fpr_list = [0.0]
    for i in np.unique(y_scores)[::-1]:
        x=[]
        for j in y_scores:
            if j < i:
                x.append(0)
            else:
                x.append(1)
        y_pred_x = np.array(x)
        y_true = np.array(y_true)
        tp = np.sum((y_pred_x == 1) & (y_true == 1))
        bottom_tpr = np.sum((y_true == 1))
        fp = np.sum((y_pred_x == 1) & (y_true == 0))
        bottom_fpr = np.sum((y_true == 0))
        tpr = tp / bottom_tpr
        fpr = fp / bottom_fpr
        tpr_list.append(tpr.item())
        fpr_list.append(fpr.item())
    return (fpr_list,tpr_list)