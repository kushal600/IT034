import numpy as np

def mcculloch_pitts_neuron(inputs, weights, threshold):
    dot_product = np.dot(inputs, weights)
    # print(dot_product)
    if dot_product == threshold:
        return 1
    else:
        return 0
      

x1x2_1= [-1,-1]
x1x2_2= [-1,1]
x1x2_3= [1,-1]
x1x2_4= [1,1]


# XOR function
print(f"XOR({x1x2_1}) = {mcculloch_pitts_neuron(x1x2_1,[1,1],0)}")
print(f"XOR({x1x2_2}) = {mcculloch_pitts_neuron(x1x2_2,[1,1],0)}")
print(f"XOR({x1x2_3}) = {mcculloch_pitts_neuron(x1x2_3,[1,1],0)}")
print(f"XOR({x1x2_4}) = {mcculloch_pitts_neuron(x1x2_4,[1,1],0)}")