from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.linear_model import SGDRegressor
import numpy as np

class Adaline:
    def __init__(self, input_size, learning_rate=0.01, epochs=50):
        self.input_size = input_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.model = SGDRegressor(max_iter=self.epochs)

    def train(self, input_data, output):
        self.model.fit(input_data, output)

    def predict(self, input_data):
        activation = self.model.predict(input_data)
        return np.where(activation >= 0.5, 1, 0)
data = load_breast_cancer()
X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

input_size = X_train.shape[1]
adaline = Adaline(input_size)
adaline.train(X_train, y_train)

y_pred = adaline.predict(X_test)
print(y_test)
print(y_pred)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))
