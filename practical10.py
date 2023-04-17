from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

mlp = MLPClassifier(hidden_layer_sizes=(30,30), activation='relu', solver='adam', max_iter=1000)

mlp.fit(X_train, y_train)

predictions = mlp.predict(X_test)
print(X_test)
print(predictions)
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
