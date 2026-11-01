import numpy as np
import math
from qsim.gates import CNOT

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

def apply_gate_fast(state, gate, targets):
    length = int(math.log2(len(state)))
    # How many axes the gates will target at once(specific handles one at a time)
    # This refactor was made to facilitate gates like CNOT that do operations on multiple qubits at once
    m = len(targets)
    
    # This makes it into a cube, or x axis
    # e.g. 3 qubits - 2x2x2
    # e.g. 4 qubits - 2x2x2x2

    dimensional_matrix = state.reshape([2] * length)

    # Reshapes gate to match m number of parallel operations on m qubits at once
    gate = gate.reshape([2] * (2 * m))

    # After tensordot, the qubits axis' get reversed due to the way gate multiplication happens with the function
    # so we have to put the qubits in the correct order thru moveaxis
    # e.g. qubit 2, then 1, then 0 appears. we reverse the axis'
    dimensional_matrix = np.tensordot(gate, dimensional_matrix, axes=(list(range(m, 2*m)), targets))
    dimensional_matrix = np.moveaxis(dimensional_matrix, list(range(m)), targets)

    result = dimensional_matrix.reshape(2**length)
    return result
    
def apply_gate_fast_specific(state, gate, k):
    if isinstance(k, (int, np.integer)):
        return apply_gate_fast(state, gate, [k])
    if isinstance(k, list):
        return apply_gate_fast(state, gate, k)
    else:
        raise TypeError('The gate number should be an integer or a list')

def apply_gate_fast_all(state, gate):
    length = int(math.log2(len(state)))
    for axis in range(length):
        state = apply_gate_fast(state, gate, [axis])

    return state