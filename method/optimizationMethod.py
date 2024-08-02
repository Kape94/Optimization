import problem.optimizationProblem as op

class Solution:
    def __init__(self, cost, spot, progressTrace):
        self.cost = cost
        self.spot = spot
        self.progressTrace = progressTrace


class OptimizationMethod:
    def run(self, problem: op.Problem) -> Solution:
        pass

