import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the input variables
water_level = ctrl.Antecedent(np.arange(0, 11, 1), 'water_level')
dirtiness_level = ctrl.Antecedent(np.arange(0, 11, 1), 'dirtiness_level')

# Define the output variable
detergent_amount = ctrl.Consequent(np.arange(0, 101, 1), 'detergent_amount')

# Define the membership functions for the input variables
water_level['low'] = fuzz.trimf(water_level.universe, [0, 0, 5])
water_level['medium'] = fuzz.trimf(water_level.universe, [0, 5, 10])
water_level['high'] = fuzz.trimf(water_level.universe, [5, 10, 10])

dirtiness_level['low'] = fuzz.trimf(dirtiness_level.universe, [0, 0, 5])
dirtiness_level['medium'] = fuzz.trimf(dirtiness_level.universe, [0, 5, 10])
dirtiness_level['high'] = fuzz.trimf(dirtiness_level.universe, [5, 10, 10])

# Define the membership functions for the output variable
detergent_amount['low'] = fuzz.trimf(detergent_amount.universe, [0, 0, 50])
detergent_amount['high'] = fuzz.trimf(detergent_amount.universe, [0, 50, 100])

# Define the rules for the fuzzy controller
rule1 = ctrl.Rule(water_level['low'] & dirtiness_level['low'], detergent_amount['low'])
rule2 = ctrl.Rule(water_level['medium'] & dirtiness_level['low'], detergent_amount['low'])
rule3 = ctrl.Rule(water_level['high'] & dirtiness_level['low'], detergent_amount['high'])
rule4 = ctrl.Rule(water_level['low'] & dirtiness_level['medium'], detergent_amount['low'])
rule5 = ctrl.Rule(water_level['medium'] & dirtiness_level['medium'], detergent_amount['high'])
rule6 = ctrl.Rule(water_level['high'] & dirtiness_level['medium'], detergent_amount['high'])
rule7 = ctrl.Rule(water_level['low'] & dirtiness_level['high'], detergent_amount['high'])
rule8 = ctrl.Rule(water_level['medium'] & dirtiness_level['high'], detergent_amount['high'])
rule9 = ctrl.Rule(water_level['high'] & dirtiness_level['high'], detergent_amount['high'])

# Create the control system
washing_machine_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

# Create the control system simulation
washing_machine = ctrl.ControlSystemSimulation(washing_machine_ctrl)

# Set the input values
washing_machine.input['water_level'] = 5
washing_machine.input['dirtiness_level'] = 7

# Compute the output value
washing_machine.compute()

# Get the output value
detergent_amount_output = washing_machine.output['detergent_amount']

print('The recommended detergent amount is', detergent_amount_output, 'percent.')
