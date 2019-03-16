from pulp import *

'''
Decision Variables
X1 = number of apples to produce
X2 = number of bananas to produce

Objective Function
MAX Profit = Revenue – Cost
= (10X1 + 6X2) – (4X1 + 3 X2)
MAX Z = 6X1 + 3X2

Constraints
X1 <= 30
X2 <= 70
X1 + X2 <= 50
X1, X2 >= 0
'''

#Decision Variable
X1 = LpVariable("Num_of_Apples",0,None)
X2 = LpVariable("Num_of_Bananas",0,None)

#Optimization Characteristics
prob = LpProblem("Maximize_Profit", LpMaximize)

#Objective Function
prob += lpSum(6*X1 + 3*X2), "Objective_Function"

#Constraints
prob += lpSum(X1) <= 30, "constraint_1"
prob += lpSum(X2) <= 70, "constraint_2"
prob += lpSum(X1+X2) <= 50, "constraint_3"

#Solver
SOLVER_PATH = r'C:\Users\Samuel\Documents\Desktop\Coin Solver\bin\cbc.exe'
prob.solve(solvers.COIN_CMD(path= SOLVER_PATH))

obj_val = value(prob.objective)
X1_val = value(X1)
X2_val = value(X2)

print(obj_val)
print(X1_val)
print(X2_val)