from qsim.circuit import Circuit
from qsim.measure import marginal_probabilities, sample
import math
import numpy as np

def build_oracle(f, n):
    size = 2 ** (n + 1)
    U = np.zeros((size, size), dtype=complex)
    for x in range(2 ** n):
        for y in [0, 1]:
            # Finds the location of |x, y> in the state vector
            col = 2 * x + y

            # output state of |x, y XOR f(x)>
            row = 2 * x + (y ^ int(f(x)))
            U[row, col] = 1

    return U

# DJ - Deutsch Jozsa
def dj_algorithmn(f, n, verbose=False):
    # Making the oracle matrix
    
    c = Circuit(n+1)
    c.x(n) # flipping the last extra bit
    for item in range(n+1):   
        c.h(item)

    # Adds the oracle as the middle operation
    c.add(build_oracle(f, n), list(range(n+1)))

    # H on only the n input qubits only
    for item in range(n):
        c.h(item)

    
    final_state = c.run(verbose=verbose)
    probs = marginal_probabilities(final_state, [item for item in range(n)])
    return "Constant" if probs[0] > 0.999 else "Balanced"

def mcz_identity(n):
    M = np.eye(2 ** n, dtype=complex)
    M[-1, -1] = -1
    return M

def grover_circuit(marked, n, iterations=None):
    if not 0 <= marked < 2 ** n:
        raise ValueError("Marked must be a valid state within the given qubits")

    if iterations == None:
        iterations = max(1, round(math.pi/ (4 * math.asin(1 / math.sqrt(2 ** n))) - 0.5))

    qubits = list(range(n))

    # Setup for the array where qubits marked state has a 0 in it(101, 10, 110, etc.)
    # This is becuz the stamping of the 'state' only works on the last state(11, or 111, or 1111 depending on the qubit count)
    # This array generates that to the desired position
    zeros = [q for q in qubits if ((marked >> (n - 1 - q)) & 1) == 0]

    c = Circuit(n)
    for item in range(n):
        c.h(item)

    for _ in range(iterations):
        # Oracle: minus signed on the |marked>
        for q in zeros: c.x(q)
        c.add(mcz_identity(n), qubits, "mcz")
        for q in zeros: c.x(q)

        # Diffusion step - reflect every amplitude about the average
        c.h_all()
        c.x_all()
        c.add(mcz_identity(n), qubits, 'mcz')
        c.x_all()
        c.h_all()        

    return c

def grover(marked, n, iterations=None, shots=500, rng=None, verbose=False):
    state = grover_circuit(marked, n, iterations).run(verbose=verbose)
    return sample(state, shots, rng)