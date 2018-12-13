from sklearn import svm
from sklearn.preprocessing import StandardScaler  
from sklearn.naive_bayes import GaussianNB 
import Evaluation as ev

def klasifikasi_svm(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()  
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)  
    X_test = scaler.transform(X_test)  
    
    # clf = svm.SVC(kernel='rbf', C = 1.0, gamma=0.02)
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, y_train)
    
    y_pred = classifier.predict(X_test)  
    precision, recall, f_measure = ev.evaluasi(y_test, y_pred)
    print("Label Test       :", y_test)
    print("Label Prediksi   :", y_pred)
    return precision, recall, f_measure

def klasifikasi_nb(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()  
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)  
    X_test = scaler.transform(X_test)  
    
    classifier = GaussianNB()  
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)  
    precision, recall, f_measure = ev.evaluasi(y_test, y_pred)
    return precision, recall, f_measure

