import numpy as np

train_A = np.array([[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1]])

train_H = np.array([[1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1]])

train_A = train_A.flatten()
train_H = train_H.flatten()

def hebb_learning_rule(train_data):
    n = len(train_data)
    weights = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                weights[i][j] = 0
            else:
                weights[i][j] += train_data[i] * train_data[j]
    return weights

weights = hebb_learning_rule(train_A)
weights += hebb_learning_rule(train_H)

test_A = np.array([1, 1, 1, 0, 1,
                   1, 0, 0, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 0, 0, 0, 1,
                   1, 0, 0, 0, 1])

test_H = np.array([1, 0, 0, 0, 1,
                   1, 0, 0, 0, 1,
                   1, 1, 1, 1, 1,
                   1, 0, 0, 0, 1,
                   1, 0, 0, 0, 1])

test_A = test_A.flatten()
test_H = test_H.flatten()

output_A = np.dot(weights, test_A)
output_H = np.dot(weights, test_H)

if np.greater(np.any(output_A) ,np.any(output_H)):
    print("Predicted letter is A")
else:
    print("Predicted letter is H")
