from sklearn.metrics import f1_score, precision_score, recall_score #, accuracy_score,  classification_report, confusion_matrix

def evaluasi(y_test, y_pred):
    f_measure = f1_score(y_test, y_pred, average="macro")
    precision = precision_score(y_test, y_pred, average="macro")
    recall    = recall_score(y_test, y_pred, average="macro")

    return precision, recall, f_measure