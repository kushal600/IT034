import numpy as np
import skfuzzy as fuzz

x = np.arange(0, 10, 1)
a = fuzz.trimf(x, [0, 2, 4])
b = fuzz.trimf(x, [1, 3, 5])

relation = np.fmax(np.minimum.outer(a, b), np.eye(len(x)))

print("Input fuzzy sets:\n", "a:", a, "\n", "b:", b)
print("\nFuzzy relation:\n", relation)
