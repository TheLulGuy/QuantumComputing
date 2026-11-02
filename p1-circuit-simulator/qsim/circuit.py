from qsim.state import zero_state
from qsim.state import apply_gate_fast_specific
from qsim.gates import H, X, Y, Z, CNOT
class Circuit:
    def __init__(self, n):
        self.n = n
        self.operations = []

    def add(self, gate, targets):
        targets = list(targets)
        for item in targets:
            if item not in range(self.n):
                raise TypeError('Emter a valid target')
        self.operations.append((gate, targets))
        return self

    def run(self):
        self.state = zero_state(self.n)
        for (gate, targets) in self.operations:
            self.state = apply_gate_fast_specific(self.state, gate, targets)

        return self.state

    def h(self, q):
        return self.add(H, [q])

    def x(self, q):
        return self.add(X, [q])

    def y(self, q):
        return self.add(Y, [q])

    def z(self, q):
        return self.add(Z, [q])

    def cx(self, c, t):
        return self.add(CNOT, (c, t))


    def gate_count(self):
        return len(self.operations)

    def depth(self):
        levels = [0] * self.n
        for(gate, targets) in self.operations:
            # Applies the max value between the targets
            layer = max(levels[q] for q in targets)
            layer += 1
            for q in targets:
                levels[q] = layer

        return max(levels)
