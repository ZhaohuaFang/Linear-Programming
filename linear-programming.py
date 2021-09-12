from scipy.optimize import minimize
import numpy as np
import random
import math

fun = lambda x: abs(x[1])
con = \
    (
        {'type': 'eq', 'fun': lambda x: x[0]},
        {'type': 'eq', 'fun': lambda x: x[10]},
        {'type': 'eq', 'fun': lambda x: x[14]},
        {'type': 'eq', 'fun': lambda x: x[6]},
        {'type': 'eq', 'fun': lambda x: x[2]},
        {'type': 'eq', 'fun': lambda x: 0.85 * x[1] - 2171.4 * x[2]},
        {'type': 'eq', 'fun': lambda x: (x[5] * (76.678 / 1000) * 89.496 / (2 * 3.1415)) - 54.304 - x[8]},

        {'type': 'eq', 'fun': lambda x: x[13] * 12500 * 3.1415 - 12500 * 3.1415 * 0.85 - x[8] * 0.85},
        {'type': 'eq', 'fun': lambda x: x[12] - x[13] + 0.85},

        {'type': 'ineq', 'fun': lambda x: x[5] - x[3] - 2.45},
        {'type': 'ineq', 'fun': lambda x: x[4] - x[5]},

        {'type': 'ineq', 'fun': lambda x: 0.1 + x[12]},
        {'type': 'ineq', 'fun': lambda x: -(x[12] - 0.1)},

        {'type': 'ineq', 'fun': lambda x: -(2.45 - x[4])},
        {'type': 'ineq', 'fun': lambda x: -(x[4] - 97.55)},
        {'type': 'ineq', 'fun': lambda x: x[3]},
        {'type': 'ineq', 'fun': lambda x: -(x[3] - 95.1)},
        {'type': 'ineq', 'fun': lambda x: x[4] - x[3] - 2.45},

    )

b = []
for i in range(15):
    a = random.random()
    b.append(a * 2)

print(b)

bounds = ((-math.inf, math.inf), (-math.inf, math.inf), (-math.inf, math.inf), (-math.inf, math.inf),
          (-math.inf, math.inf), (-math.inf, math.inf), (-math.inf, math.inf), (-math.inf, math.inf),
          (-math.inf, math.inf),
          (-math.inf, math.inf), (-math.inf, math.inf), (-math.inf, math.inf), (-math.inf, math.inf),
          (-math.inf, math.inf), (-math.inf, math.inf))
res = minimize(fun, b, method='SLSQP', constraints=con, bounds=bounds)
print(res)
