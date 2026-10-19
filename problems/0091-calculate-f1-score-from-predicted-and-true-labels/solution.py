import numpy as np

def calculate_f1_score(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    top = np.sum((y_pred == 1) & (y_true == y_pred)).item()
    prec_bottom = np.sum(y_pred == 1).item()
    rec_bottom = np.sum(y_true == 1).item()

    if top == 0 or prec_bottom == 0 or rec_bottom == 0:
        return 0.0

    prec = top / prec_bottom
    rec = top / rec_bottom
    f1 = 2 * prec * rec / (rec + prec)
    return round(f1, 3)