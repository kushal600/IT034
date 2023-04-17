import matplotlib.pyplot as plt
import numpy as np

# Define the parameters of the triangular fuzzy membership function
a = 0
b = 5
c = 2.5
d=3.5

# Define the universe of discourse
x = np.linspace(0, 5, 100)

# Define the triangular fuzzy membership function
mu = np.zeros_like(x)
mu[(x >= a) & (x < c)] = (x[(x >= a) & (x < c)] - a) / (c - a)
mu[(x >= c) & (x <= b)] = (b - x[(x >= c) & (x <= b)]) / (b - c)

# Define trapozodial membership function 
nu = np.zeros_like(x)
nu[(x >= a) & (x < c)] = (x[(x >= a) & (x < c)] - a) / (c - a)
nu[(x >= c) & (x <= d)] = 1
nu[(x > d) & (x <= b)] = (b - x[(x > d) & (x <= b)]) / (b - d)
# Plot the triangular fuzzy membership function
plt.plot(x, mu, label='Triangular Fuzzy Membership Function')
plt.xlabel('x')
plt.ylabel('Membership Degree')
plt.title('Triangular Fuzzy Membership Function')
plt.plot(x, nu, label='Trapezoidal Fuzzy Membership Function')
plt.xlabel('x')
plt.ylabel('Membership Degree')
plt.title('Trapezoidal Fuzzy Membership Function')
# plt.legend()
plt.legend()
plt.show()
