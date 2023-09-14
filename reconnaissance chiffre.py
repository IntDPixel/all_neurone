from sklearn import datasets
digits = datasets.load_digits()

print(digits.images[0])

import matplotlib.pyplot as plt
plt.imshow(digits.images[0],cmap='binary')
plt.title(digits.target[0])
plt.axis('off')
plt.show()

x = digits.images.reshape((len(digits.images), -1))
# x contient toutes les images en version 1D.
# nous imprimons ici la première, que nous avons déjà vue : 
print(x[0])

y = digits.target

from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(15,))

x_train = x[:1000]
y_train = y[:1000]
x_test = x[1000:]
y_test = y[1000:]

mlp.fit(x_train, y_train)
mlp.predict(x_test[:10])
y_test[:10]
y_pred = mlp.predict(x_test)
error = (y_pred != y_test)
import numpy as np
np.sum(error) / len(y_test)
x_error = x_test[error].reshape((-1, 8,8))
y_error = y_test[error]
y_pred_error = y_pred[error]
i = 10
plt.imshow(x_error[i],cmap='binary')
plt.title(f'cible: {y_error[i]}, prediction: {y_pred_error[i]}')
plt.axis('off')
plt.show()
