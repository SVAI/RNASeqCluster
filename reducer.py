import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

plotColors = ['ro', 'bo', 'go', 'wo', 'yo']
markerColors = ['red', 'blue', 'green', 'black', 'yellow']

class Reducer:
    def __init__():
        pass

    def reduce(data):
        pass

###################
class TSNE(Reducer):
    def __init__():
        pass

    def reduce(data, n):
        model = TSNE(n_components=n, random_state=0)
        np.set_printoptions(suppress=True)
        arr = model.fit_transform(X)
        x, y = zip(*arr)
        pass

###################
class PCA(Reducer):
    def __init__():
        pass

    def reduce(data):
        pass

###################
class ICA(Reducer):
    def __init__():
        pass

    def reduce(data):
        pass

###################
class TopKExpansion(Reducer):
    def __init__():
        pass

    def reduce(data):
        pass
