import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def fitness(x):
    return -x**2

varbound = np.array([[0, 20]])

model = ga(function=fitness, dimension=1, variable_type='real', variable_boundaries=varbound)

model.run(max_iter=5)

fittest_individual = model.best_variable[0]
print('Fittest individual:', fittest_individual, 'Fitness:', -model.best_function)
