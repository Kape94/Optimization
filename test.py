import problem.optimizationTestFunctions as problems

import method.seekCurrentBest as seekCurrentBest
import method.pso as pso

import benchmark

import numpy as np
import matplotlib.pyplot as plt

rosenbrock2D = problems.rosenbrockProblem(2)
method = seekCurrentBest.seekCurrentBest(3, 100)

summary = benchmark.doTest(100, rosenbrock2D, method)

bestValues = summary.solutionsValues()
print("--------------DONE---------------------")
print("Min:", np.min(bestValues))
print("Max:", np.max(bestValues))
print("Mean:", np.mean(bestValues))
print("Std:", np.std(bestValues))

plt.plot(summary.bestSolution().progressTrace)
plt.show()