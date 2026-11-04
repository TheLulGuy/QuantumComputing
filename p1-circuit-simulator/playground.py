from qsim.state import *
from qsim.gates import *
from qsim.measure import *
from qsim.circuit import Circuit
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

    '''
    000   000
    001   001
    010   011
    011   010
    100   101
    101   100
    110   110
    111   111
    '''

# dj_algorithmn(lambda x : 0, 2)
# dj_algorithmn(lambda x : 1, 2)
result = dj_algorithmn(lambda x: (x & 1) ^ (x >> 1), 1, True)
print(result)