import numpy as np
from collections import Counter


def dis_euc(x1, x2):
    distance = np.sqrt(np.sum((x1-x2)**2))
    return distance


class KNN:
        def __init__(self, k=3):
                self.k = k

        def fit(self, X, y):
                self.X_train = X
                self.y_train = y
        
        def predict(self, X):
                predicciones = [self.predicthelper(x) for x in X]
                return predicciones
        
        def predicthelper(self, x): #la x minúscula representa un único punto del cual se quiere saber la distancia respecto al resto.
                # calcuar las distancia con la euclidiana
                distancias = [dis_euc(x, x_train)for x_train in self.X_train] 


                # obtener la k más cercana 

                k_indices = np.argsort(distancias)[:self.k]
                k_cercanos = [self.y_train[i] for i in k_indices]

                # majority vote
                mas_comunes = Counter(k_cercanos).most_common()
                return mas_comunes[0][0]