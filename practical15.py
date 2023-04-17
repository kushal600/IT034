import numpy as np

R = np.array([[0.0, 0.5, 1.0, 0.9, 0.2],
              [0.8, 1.0, 0.4, 0.7, 0.9],
              [0, 0, 1.0, 0, 0],
              [0.1, 0, 0, 1.0, 0.5],
              [0.2, 0.9, 0, 0.5, 1.0]])

is_reflexive = np.all(np.diag(R) == 1)
is_symmetric = np.all(R == R.T)
is_transitive = np.all(np.fmax(R @ R, R) == R)

is_equivalence = is_reflexive and is_symmetric and is_transitive

print("Fuzzy relation R:\n", R)
print("\nIs R reflexive?", is_reflexive)
print("Is R symmetric?", is_symmetric)
print("Is R transitive?", is_transitive)
print("Is R an equivalence relation?", is_equivalence)
