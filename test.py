import numpy as np
# Constants
h_max = 1.0 # Maximum water level (m)
h_min = 0.0 # Minimum water level (m)
h_sp = 0.5 # Set point (m)
f_min = 0.0 # Minimum flow rate (m3/s)
f_max = 0.1 # Maximum flow rate (m3/s)
Kp = 1.0 # Proportional gain
Ki = 1.0 # Integral gain
Ts = 0.1 # Sampling time (s)
# Initialize state variables
h = h_min # Water level (m)
e_int = 0.0 # Integral error
f_in = f_min # Inlet flow rate (m3/s)
# Define neural controller weights and bias
w1 = np.array([-1.0, 1.0])
w2 = np.array([0.5, 0.5])

b1 = -0.5
# Define activation function
def sigmoid(x):
  return 1.0 / (1.0 + np.exp(-x))
# Control loop
for t in np.arange(0.0, 10.0, Ts):
# Calculate error
  e = h_sp - h
  # Calculate integral error
  e_int += e * Ts
  # Calculate control signal using neural controller
  x = np.array([e, e_int])
  z = sigmoid(np.dot(w1, x) + b1)
  f_out = f_min + (f_max - f_min) * sigmoid(np.dot(w2, z))
  # Apply control signal to system
  h += (f_in - f_out) * Ts
  # Clip water level to [h_min, h_max] range
  h = np.clip(h, h_min, h_max)
  # Update inlet flow rate
  f_in += Kp * (f_max - f_out) + Ki * e_int
  # Clip inlet flow rate to [f_min, f_max] range
  
  f_in = np.clip(f_in, f_min, f_max)
  # Print current time and water level
  print("t = {:.1f}, h = {:.2f}".format(t, h))