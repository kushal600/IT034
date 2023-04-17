from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_classes=4, n_features=4, n_informative=2, n_redundant=2, random_state=42, n_clusters_per_class=1)
clf = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
clf.fit(X, y)
accuracy = clf.score(X, y)
print("Accuracy:", accuracy)
