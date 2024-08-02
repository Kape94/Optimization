import numpy as np

import method.optimizationMethod as om
import problem.optimizationProblem as op

class pso(om.OptimizationMethod):
    def __init__(self, n, w, c1, c2, maxIterations) -> None:
        self.n = n
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.maxIterations = maxIterations


    def run(self, problem: op.Problem) -> om.Solution:
        costFunction = problem.func()
        bounds = problem.bounds()

        infBound = bounds[0]
        supBound = bounds[1]
        searchRange = supBound - infBound
        d = infBound.size

        populationSize = self.n
        inertiaWeight = self.w
        c1 = self.c1
        c2 = self.c2

        p = np.zeros([populationSize, d])
        
        v = np.copy(p)
        for i in range(0, populationSize):
            p[i] = infBound + np.multiply(np.random.rand(d), searchRange) 
            v[i] = 0.0

        pBest = np.copy(p)
        pBestCost = np.zeros(populationSize)
        gBest = np.copy(pBest[0])
        gBestCost = costFunction(gBest)
        
        progressTrace = []

        nIterations = self.maxIterations
        for i in range(0, nIterations):
            #evaluate the cost function and update pBest and gBest
            for i in range(0, populationSize):
                pBestCost[i] = costFunction(pBest[i])
                if pBestCost[i] < gBestCost:
                    gBest = np.copy(pBest[i])
                    gBestCost = pBestCost[i]
            
            progressTrace.append(gBestCost)

            #calculate velocity and update position
            for i in range(0, populationSize):
                r1 = np.random.rand(d)
                r2 = np.random.rand(d)

                cognitiveMovement = c1 * r1 * (pBest[i] - p[i])
                socialMovement = c2 * r2 * (gBest - p[i])
                v[i] = (inertiaWeight * v[i]) + cognitiveMovement + socialMovement
                p[i] = p[i] + v[i]

        return om.Solution(gBestCost, gBest, progressTrace)
