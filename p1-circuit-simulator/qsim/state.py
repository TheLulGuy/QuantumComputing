import numpy as np

def zero_state(n):
    # initializing 2**n number of 0's, for n number of qubits
    state = np.zeros(2**n, dtype=complex)

    # First state is 1, as the probability of the first state being a 0 is 100%
    # quantum computers always start on a 0, thus the amplitude in the beginning will always be a 0
    # the rest have a probability of 0% for being a 0, as the amplitudes have now started oscillating
    state[0] = 1
    return state

def apply_1q(state, gate):
    # Matrix multiplication symbol is @
    return state @ gate