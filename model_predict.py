from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import sklearn as sk
import seaborn as sns
import numpy as np

def train_and_evaluate_models(x, y, data_name):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    models = {
        'SVM': SVC(),
        'Random Forest': RandomForestClassifier(),
        'KNN': KNeighborsClassifier()
    }
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)
        
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y), yticklabels=np.unique(y))
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title(f'{data_name}, '
                  f'acc.: {model.score(X_test, y_test):.2f}, '
                  f'prec.: {sk.metrics.precision_score(y_test, y_pred):.2f}, '
                  f'rec.: {sk.metrics.recall_score(y_test, y_pred):.2f}, '
                  f'f1: {sk.metrics.f1_score(y_test, y_pred):.2f}')
        plt.show()