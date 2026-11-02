from qsim.state import zero_state
from qsim.state import apply_gate_fast_specific
from qsim.gates import H, X, Y, Z, CNOT
class Circuit:
    def __init__(self, n):
        self.n = n
        self.operations = []


    def add(self, gate, targets):
        targets = list(targets)
        self.operations.append((gate, targets))
        return self

    def run(self):
        self.state = zero_state(self.n)
        for (gate, targets) in self.operations:
            self.state = apply_gate_fast_specific(self.state, gate, targets)

        return self.state

    def h(self, q):
        self.add(H, [q])
        return self

    def x(self, q):
        self.add(X, [q])
        return self

    def y(self, q):
        self.add(Y, [q])
        return self

    def z(self, q):
        self.add(Z, [q])
        return self

    def cx(self, c, t):
        self.add(CNOT, (c, t))
        return self