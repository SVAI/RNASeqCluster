import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

plotColors = ['ro', 'bo', 'go', 'wo', 'yo']
markerColors = ['red', 'blue', 'green', 'black', 'yellow']

X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
model = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)
arr = model.fit_transform(X) 

x, y = zip(*arr)

fig = plt.figure()
fig.suptitle('test', fontsize=14, fontweight='bold')
plt.plot(x, y, plotColors[0])
plt.show()
