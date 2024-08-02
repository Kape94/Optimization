import numpy as np

import problem.optimizationProblem as op

class TestFunctionProblem(op.Problem):
    def __init__(self, func, bounds):
        self._func = func
        self._bounds = bounds

    def func(self):
        return self._func
    
    def bounds(self):
        return self._bounds


# -------------------------- Rosenbrock ------------------------------
def rosenbrockProblem(nDimensions):
    bounds = hypercubeBounds(-2.048, 2.048, nDimensions)
    return TestFunctionProblem(rosenbrock, bounds)

def rosenbrock(x):
    n = x.size
    x_iPlus1 = x[1:n]
    x_i = x[0:n-1]

    x_iSqr = np.pow(x_i, 2)
    firstPart = 100 * np.pow(x_iPlus1 - x_iSqr, 2)
    secondPart = np.pow(x_i - 1, 2)
    total = firstPart + secondPart
    return np.sum(total)
# ---------------------------------------------------------------------

# ------------------------ Schwefell 2.26 -----------------------------
def schwefell226Problem(nDimensions):
    bounds = hypercubeBounds(-500, 500, nDimensions)
    return TestFunctionProblem(schwefell226, bounds)

def schwefell226(x):
    d = x.size
    
    modulation = np.sin(np.sqrt(np.abs(x)))
    productArray = np.multiply(x, modulation)
    sum = np.sum(productArray)

    return (418.9829 * d) - sum
# ---------------------------------------------------------------------

# ===================== Utility functions ===========================

def hypercubeBounds(infValue, supValue, nDimensions):
    infBnd = np.ones(nDimensions) * infValue
    supBnd = np.ones(nDimensions) * supValue
    
    return np.array([infBnd, supBnd])

