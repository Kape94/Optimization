import numpy as np

import method.optimizationMethod as om
import problem.optimizationProblem as op

class seekCurrentBest(om.OptimizationMethod):
    def __init__(self, n, maxIterations):
        self.n = n
        self.maxIterations = maxIterations

    def run(self, problem: op.Problem) -> om.Solution:
        costFunction = problem.func()
        bounds = problem.bounds()

        infBound = bounds[0]
        supBound = bounds[1]
        searchRange = supBound - infBound
        d = infBound.size

        populationSize = self.n

        p = np.zeros([populationSize, d])

        for i in range(0, populationSize):
            p[i] = infBound + np.multiply(np.random.rand(d), searchRange)

        best = np.copy(p[0])
        bestEval = costFunction(best)

        progressTrace = []
        
        nIterations = self.maxIterations
        for i in range(0, nIterations):
            for i in range(0, populationSize):
                pEval = costFunction(p[i])
                if (pEval < bestEval):
                    bestEval = pEval
                    best = np.copy(p[i])
            
            progressTrace.append(bestEval)

            for i in range(0, populationSize):
                p[i] = p[i] + np.random.rand() * (best - p[i]) 

        return om.Solution(bestEval, best, progressTrace)
