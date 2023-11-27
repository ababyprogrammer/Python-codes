import scipy.optimize

# Objective Function: 50x_1 + 80x_2
# Constraint 1: 5x_1 + 2x_2 <= 20
# Constraint 2: -10x_1 + -12_2 <= -90

result = scipy.optimize.linprog(
    [50, 80],
    A_ub=[[5, 8], [-10, -12]],
    b_ub=[20, -90]
)

if result.success:
    print(f"X1: {round(result.x[0], 2)} hours")
    print(f"X2: {round(result.x[1], 2)} hours")
else:
    print("No solution")