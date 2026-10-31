import numpy as np
import math

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
    return gate @ state

# Prototype for making a universal gate
def apply_gate_all(state, gate):
    length = int(math.log2(len(state)))

    final_gate = 1
    for item in range(length):
        final_gate = np.kron(final_gate, gate)

    return final_gate @ state

def apply_gate_specific(state, gate, k):
    length = int(math.log2(len(state)))
    I = np.eye(2, dtype=complex)
    final_gate = 1
    for index in range(length):
        if index == k:
            temp = gate
        else:
            temp = I
        final_gate = np.kron(final_gate, temp)
    return final_gate @ state
