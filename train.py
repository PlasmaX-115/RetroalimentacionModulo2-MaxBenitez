import numpy as np
from KNN import KNN
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

#Se carga el dataset de iris
iris = datasets.load_iris()

#Se carga el dataset de digits
digits = datasets.load_digits()

# Generar predicciones con el dataset iris
X,y = iris.data, iris.target

# Generar predicciones con el dataset digits
# X,y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

plt.figure()
plt.scatter(X[:,2], X[:,3], c=y, cmap = cmap, edgecolor='k', s=20)
plt.show()


clf = KNN(k=5)
clf.fit(X_train, y_train)
predicciones = clf.predict(X_test)

print(classification_report(y_test,predicciones))

# Matriz de confusión para el dataset de iris.

cm = confusion_matrix(y_test, predicciones)

df1 = pd.DataFrame(columns=["0","1","2",], index= ["0","1","2"], data= cm )

f,ax = plt.subplots(figsize=(3,3))

sns.heatmap(df1, annot=True,cmap="Greens", fmt= '.0f',
            ax=ax,linewidths = 5, cbar = False,annot_kws={"size": 14})
plt.xlabel("Predicted Label")
plt.xticks(size = 10)
plt.yticks(size = 10, rotation = 0)
plt.ylabel("True Label")
plt.title("Confusion Matrix", size = 10)
plt.show()


print(predicciones)

accuracy = np.sum(predicciones == y_test)/ len(y_test)
print(accuracy)