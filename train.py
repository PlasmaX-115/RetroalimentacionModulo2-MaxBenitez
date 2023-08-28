import numpy as np
from KNN import KNN
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

#Se carga el dataset de iris
iris = datasets.load_iris()

#Se carga el dataset de digits
digits = datasets.load_digits()

# Generar predicciones con el dataset iris
# X,y = iris.data, iris.target

# Generar predicciones con el dataset digits
X,y = digits.data, digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

plt.figure()
plt.scatter(X[:,2], X[:,3], c=y, cmap = cmap, edgecolor='k', s=20)
plt.show()


clf = KNN(k=5)
clf.fit(X_train, y_train)
predicciones = clf.predict(X_test)

print(predicciones)

accuracy = np.sum(predicciones == y_test)/ len(y_test)
print(accuracy)