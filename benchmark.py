import problem.optimizationProblem as op
import method.optimizationMethod as om

class summary:
    def __init__(self) -> None:
        self._solutionsValues: list = []
        self._bestSolution: om.Solution = None

    def update(self, solution: om.Solution):
        self._solutionsValues.append(solution.cost)
        if self._shouldReplaceCurrentBest(solution):
            self._bestSolution = solution

    def _shouldReplaceCurrentBest(self, solution: om.Solution):
        currentBestIsNull = self._bestSolution == None
        return currentBestIsNull or solution.cost < self._bestSolution.cost
    
    def bestSolution(self) -> om.Solution:
        return self._bestSolution
    
    def solutionsValues(self) -> list:
        return self._solutionsValues


def doTest(nRuns, problem: op.Problem, method: om.OptimizationMethod) -> summary:
    s = summary()

    for i in range(0, nRuns):
        sol = method.run(problem)
        s.update(sol)

    return s