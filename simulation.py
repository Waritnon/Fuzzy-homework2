import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

##create fuzzy
laundry_weight = ctrl.Antecedent(np.arange(0, 11, 1), 'laundry_weight')
detergent_concentration = ctrl.Antecedent(np.arange(0, 101, 1), 'detergent_concentration')
washing_time = ctrl.Consequent(np.arange(0, 101, 1), 'washing_time')

##define membership 
laundry_weight['light'] = fuzz.trimf(laundry_weight.universe, [0, 0, 5])
laundry_weight['medium'] = fuzz.trimf(laundry_weight.universe, [0, 5, 10])
laundry_weight['heavy'] = fuzz.trimf(laundry_weight.universe, [5, 10, 10])

detergent_concentration['low'] = fuzz.trimf(detergent_concentration.universe, [0, 0, 50])
detergent_concentration['high'] = fuzz.trimf(detergent_concentration.universe, [0, 50, 100])

washing_time['short'] = fuzz.trimf(washing_time.universe, [0, 0, 50])
washing_time['long'] = fuzz.trimf(washing_time.universe, [0, 50, 100])

##define rules
rule1 = ctrl.Rule(laundry_weight['light'] & detergent_concentration['low'], washing_time['short'])
rule2 = ctrl.Rule(laundry_weight['light'] & detergent_concentration['high'], washing_time['short'])
rule3 = ctrl.Rule(laundry_weight['medium'] & detergent_concentration['low'], washing_time['short'])
rule4 = ctrl.Rule(laundry_weight['medium'] & detergent_concentration['high'], washing_time['long'])
rule5 = ctrl.Rule(laundry_weight['heavy'] & detergent_concentration['low'], washing_time['long'])
rule6 = ctrl.Rule(laundry_weight['heavy'] & detergent_concentration['high'], washing_time['long'])

##control system
washing_machine_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])

##simulation
washing_machine = ctrl.ControlSystemSimulation(washing_machine_ctrl)

##Input(can change)
washing_machine.input['laundry_weight'] = 2
washing_machine.input['detergent_concentration'] = 27

##computing
washing_machine.compute()

##showing output
print("Recommended washing time:" , washing_machine.output['washing_time'])
washing_time.view(sim=washing_machine)
plt.show()

