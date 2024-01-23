# Import necessary libraries
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def classification_model_evaluation(y_test, y_pred):
    # Model Evaluation
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)
    return accuracy, conf_matrix, classification_rep