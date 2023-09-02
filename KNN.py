#----------------------------------------------------------
#
# Date: 28-Aug-2023
#
#           A01752791 Maximiliano Benítez Ahumada
#----------------------------------------------------------


import numpy as np
from collections import Counter

def dis_euc(x1, x2):
    """
    Calcula la distancia euclidiana entre dos puntos.

    Args:
    - x1 (array-like): Coordenadas del primer punto.
    - x2 (array-like): Coordenadas del segundo punto.

    Returns:
    - float: La distancia euclidiana entre los dos puntos.
    """
    distance = np.sqrt(np.sum((x1 - x2) ** 2))
    return distance


class KNN:
    """
    Implementación del algoritmo K-Nearest Neighbors (KNN).

    K-Nearest Neighbors es un algoritmo de aprendizaje supervisado utilizado
    para clasificación.

    Args:
    - k (int): Número de vecinos cercanos a considerar en la predicción (por defecto, 3).

    Métodos:
    - fit(X, y): Entrena el modelo KNN con datos de entrenamiento.
    - predict(X): Realiza predicciones sobre un conjunto de datos de prueba.

    Ejemplo de uso:

    >>> clf = KNN(k=5)
    >>> clf.fit(X_train, y_train)
    >>> predictions = clf.predict(X_test)
    """

    def __init__(self, k=3):
        """
        Inicializa una instancia de la clase KNN con el número de vecinos a considerar.

        Args:
        - k (int): Número de vecinos cercanos a considerar en la predicción (por defecto, 3).
        """
        self.k = k

    def fit(self, X, y):
        """
        Entrena el modelo KNN con datos de entrenamiento.

        Args:
        - X (array-like): Conjunto de datos de entrenamiento, donde cada fila representa una instancia.
        - y (array-like): Etiquetas correspondientes a las instancias de entrenamiento.
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """
        Realiza predicciones sobre un conjunto de datos de prueba.

        Args:
        - X (array-like): Conjunto de datos de prueba, donde cada fila representa una instancia.

        Returns:
        - list: Predicciones para cada instancia de prueba.
        """
        predicciones = [self.predicthelper(x) for x in X]
        return predicciones

    def predicthelper(self, x):
        """
        Realiza una predicción para un punto de datos específico.

        Args:
        - x (array-like): Punto de datos para el que se desea hacer una predicción.

        Returns:
        - int: Etiqueta predicha para el punto de datos.
        """
        # Calcular las distancias utilizando la distancia euclidiana
        distancias = [dis_euc(x, x_train) for x_train in self.X_train]

        # Obtener los índices de los k vecinos más cercanos
        k_indices = np.argsort(distancias)[:self.k]

        # Obtener las etiquetas de los k vecinos más cercanos
        k_cercanos = [self.y_train[i] for i in k_indices]

        # Realizar el voto mayoritario para determinar la etiqueta predicha
        mas_comunes = Counter(k_cercanos).most_common()
        return mas_comunes[0][0]
