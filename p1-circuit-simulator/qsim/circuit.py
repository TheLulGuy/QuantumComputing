from qsim.state import zero_state
from qsim.state import apply_gate_fast_specific
from qsim.gates import H, X, Y, Z, CNOT

class Circuit:
    def __init__(self, n):
        self.n = n
        self.operations = []

    def add(self, gate, targets, name='CUSTOM'):
        if not isinstance(targets, list):
            targets = list(targets)

        for item in targets:
            if item not in range(self.n):
                raise TypeError('Enter a valid target')
        self.operations.append((gate, targets, name))
        return self

    def run(self, verbose=False):
        self.state = zero_state(self.n)
        if verbose:
            for index, (gate, targets, name) in enumerate(self.operations):
                self.state = apply_gate_fast_specific(self.state, gate, targets)
                print(index, f'--{name}-->', self.state)
        else:
            for (gate, targets, _) in self.operations:
                self.state = apply_gate_fast_specific(self.state, gate, targets)

        return self.state

    def h(self, q):
        return self.add(H, [q], 'H')

    def x(self, q):
        return self.add(X, [q], 'X')

    def y(self, q):
        return self.add(Y, [q], 'Y')

    def z(self, q):
        return self.add(Z, [q], 'Z')

    def cx(self, c, t):
        return self.add(CNOT, (c, t), 'CNOT')


    def gate_count(self):
        return len(self.operations)

    def depth(self):
        levels = [0] * self.n
        for(_, targets, _) in self.operations:
            # Applies the max value between the targets
            layer = max(levels[q] for q in targets)
            layer += 1
            for q in targets:
                levels[q] = layer

        return max(levels)
