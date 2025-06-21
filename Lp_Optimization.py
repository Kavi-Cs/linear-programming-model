import pulp as p

# Create LP Maximization problem
Lp_prob = p.LpProblem('Problem1', p.LpMaximize)

# Decision Variables
x1 = p.LpVariable("x1", lowBound=0)
x2 = p.LpVariable("x2", lowBound=0)
x3 = p.LpVariable("x3", lowBound=0)

# Objective Function
Lp_prob += 1600 * x1 + 1300 * x2 + 600 * x3

# Constraints
Lp_prob += 2 * x1 + 1.5 * x2 + x3 <= 20
Lp_prob += 2 * x1 + x2 + 1.5 * x3 <= 24
Lp_prob += x1 + 2 * x2 + 0.5 * x3 <= 20

# Solve the problem
status = Lp_prob.solve()

# Output results
print("Status:", p.LpStatus[status])
print("Optimal Solution:")
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"x3 = {x3.varValue}")
print("Maximum_Profit =", p.value(Lp_prob.objective))

