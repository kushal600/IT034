import numpy as np

def mcculloch_pitts_neuron(inputs, weights, threshold):
    dot_product = np.dot(inputs, weights)
    # print(dot_product)
    if dot_product >= threshold:
        return 1
    else:
        return 0
      

x1x2_1= [0,0]
x1x2_2= [0,1]
x1x2_3= [1,0]
x1x2_4= [1,1]


# And function
print(f"AND({x1x2_1}) = {mcculloch_pitts_neuron(x1x2_1,[1,1],2)}")# x_and = np.array([0, 1])
print(f"AND({x1x2_2}) = {mcculloch_pitts_neuron(x1x2_2,[1,1],2)}")# x_and = np.array([0, 1])
print(f"AND({x1x2_3}) = {mcculloch_pitts_neuron(x1x2_3,[1,1],2)}")# x_and = np.array([0, 1])
print(f"AND({x1x2_4}) = {mcculloch_pitts_neuron(x1x2_4,[1,1],2)}")# x_and = np.array([0, 1])

# OR function
print(f"OR({x1x2_1}) = {mcculloch_pitts_neuron(x1x2_1,[1,1],1)}")# x_and = np.array([0, 1])
print(f"OR({x1x2_2}) = {mcculloch_pitts_neuron(x1x2_2,[1,1],1)}")# x_and = np.array([0, 1])
print(f"OR({x1x2_3}) = {mcculloch_pitts_neuron(x1x2_3,[1,1],1)}")# x_and = np.array([0, 1])
print(f"OR({x1x2_4}) = {mcculloch_pitts_neuron(x1x2_4,[1,1],1)}")# x_and = np.array([0, 1])

# NOT function
print(f"NOT({x1x2_1[0]}) = {mcculloch_pitts_neuron(x1x2_1[0],[-1],0)}")# x_and = np.array([0, 1])
print(f"NOT({x1x2_3[0]}) = {mcculloch_pitts_neuron(x1x2_3[0],[-1],0)}")# x_and = np.array([0, 1])



