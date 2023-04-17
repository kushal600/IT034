import numpy as np
import matplotlib.pyplot as plt


def identity(x):
    return x

def linear(x):
    return 2*x

def binary_step(x):
    return np.heaviside(x, 1)

def bipolar_step(x):
    return np.heaviside(x, 1) * 2 - 1

def bell_shaped(x, a=1, b=1, c=0):
    return 1 / (1 + np.power((x-c)/a, 2*b))


x = np.linspace(-5, 5, 1000)

y_identity = identity(x)
y_linear = linear(x)
y_binary_step = binary_step(x)
y_bipolar_step = bipolar_step(x)
y_bell_shaped = bell_shaped(x, a=1, b=1, c=0)



fig, ax = plt.subplots(figsize=(6,6))

ax.plot(x, y_identity, label='Identity')
ax.plot(x, y_linear, label='Linear')
ax.plot(x, y_binary_step, label='Binary Step')
ax.plot(x, y_bipolar_step, label='Bipolar Step')
ax.plot(x, y_bell_shaped, label='Bell-Shaped')

ax.set_xlim([-5, 5])
ax.set_ylim([-1.5, 1.5])

ax.legend()
ax.grid(True)

plt.show()
