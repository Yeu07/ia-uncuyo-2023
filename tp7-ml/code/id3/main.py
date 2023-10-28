import pandas as pd
from decision_tree import *
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("tp7-ml/data/tennis.csv")
confusion_matrix_ = [[0, 0], [0, 0]]
n=250
i=0
sum=0
while i < n:
    train = data.sample(frac=0.8)
    test = data.drop(train.index)
    tree = decision_tree(train, "play")
    canPredict = predict(tree, test, "play")
    
    if canPredict:
        true = test["play"].tolist()
        pred = test["prediction"].tolist()
        
        # Calcula la matriz de confusión para esta iteración y agrega los resultados
        confusion_matrix_it = confusion_matrix(true, pred)
        confusion_matrix_ += confusion_matrix_it
        
        acc = accuracy_score(true, pred)
        sum += acc
        i += 1

avg = sum / n
print("Average accuracy:", avg)
confusion_df = pd.DataFrame(confusion_matrix_, columns=[" Prediction 0", " Prediction 1"], index=["Real 0", "Real 1"])
print(confusion_df)
