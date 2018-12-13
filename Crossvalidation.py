import numpy as np
from sklearn.model_selection import KFold
import Classification as cl

def crossvalidation(df):
    y = df.iloc[:,-1:].values.ravel()                      # tabel label sesuai data ekstraksi
    X = df.iloc[:,0:-1].values        
    
    kf = KFold(n_splits=10, shuffle=False) 
    arr_precision, arr_recall, arr_f_measure = [], [], []
    count = 0
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index] 
        y_train, y_test = y[train_index], y[test_index]
        
        print("Fold Ke-",count+1)
#        print("Index Data Latih     : ", train_index)
#        print("Index Data Uji       : ", test_index)
    
        # PROSES KLASIFIKASINYA DISINI
        # print("===       Naive Bayes      ===")
        #precision, recall, f_measure = cl.klasifikasi_nb(X_train, X_test, y_train, y_test)
        # print("=== Support Vector Machine ===")
        precision, recall, f_measure = cl.klasifikasi_svm(X_train, X_test, y_train, y_test)
        arr_precision.append(precision)
        arr_recall.append(recall)
        arr_f_measure.append(f_measure)
        count += 1
        
    rata_precision  = np.mean(arr_precision)
    rata_recall     = np.mean(arr_recall)
    rata_fmeasure   = np.mean(arr_f_measure)
    
    return rata_precision, rata_recall, rata_fmeasure