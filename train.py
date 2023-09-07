#----------------------------------------------------------
#
# Date: 28-Aug-2023
#
#           A01752791 Maximiliano Benítez Ahumada
#----------------------------------------------------------

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

# Se carga el dataset de iris
iris = datasets.load_digits()

# Generar predicciones con el dataset iris
X, y = iris.data, iris.target

# Número de iteraciones para diferentes semillas aleatorias
num_iterations = 10

# Crear una sola figura con 10 subplots
fig, axs = plt.subplots(2, 5, figsize=(15, 8))

for iteration in range(num_iterations):
    print(f"Iteration {iteration + 1}:")

    # Dividir los datos en conjuntos de entrenamiento y prueba con una semilla aleatoria diferente en cada iteración
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=iteration)

    clf = KNN(k=5)  # Crear una instancia del clasificador KNN
    clf.fit(X_train, y_train)  # Entrenar el modelo KNN
    predicciones = clf.predict(X_test)  # Realizar predicciones

    print(classification_report(y_test, predicciones))  # Imprimir informe de clasificación

    # Matriz de confusión para el dataset de iris
    cm = confusion_matrix(y_test, predicciones)

    # Crear un DataFrame de pandas para la matriz de confusión con etiquetas dinámicas
    num_classes = len(np.unique(y_test))
    class_labels = [str(i) for i in range(num_classes)]
    df1 = pd.DataFrame(columns=class_labels, index=class_labels, data=cm)


    row, col = divmod(iteration, 5)  # Calcular la posición del subplot
    ax = axs[row, col]

    sns.heatmap(df1, annot=True, cmap="Greens", fmt='.0f',
                ax=ax, linewidths=5, cbar=False, annot_kws={"size": 14})
    ax.set_xlabel("Predicted Label")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylabel("True Label")
    ax.set_title(f"Iteration {iteration + 1}", size=10)

    accuracy = np.sum(predicciones == y_test) / len(y_test)
    print(f"Accuracy: {accuracy}\n")

# Ajustar el diseño de los subplots
plt.tight_layout()
plt.show()
