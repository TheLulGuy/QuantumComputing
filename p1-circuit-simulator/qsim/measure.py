import numpy as np
import math

def probabilities(state):
    return np.abs(state) ** 2

def sample(state, shots, rng=None):
    """Goes thru 'shots' number of iterations on the state to see how many times each state comes up
    (basically a dice roll with qubits)"""
    n = int(math.log2(len(state)))

    # Initialize random state, taking None or integer as the seed
    rng = np.random.default_rng(rng)

    # Runs the dice roll according to the state, shots and probabilities
    outcomes = rng.choice(len(state), size=shots, p=probabilities(state))
    # Counts how many times each index comes up(thus unique), and returns it as a dictionary
    indices, counts = np.unique(outcomes, return_counts=True)

    # Formats the output
    counts_by_bitstring = {}
    for index, count in zip(indices, counts):
        # Converts each index to its bit counterpart
        #? format(1, '02b') --> 01
        #? format(4, '03b') --> 100
        bitstring = format(int(index), f"0{n}b")
        counts_by_bitstring[bitstring] = int(count)

    return counts_by_bitstring

def marginal_probabilities(state, qubits):
    qubits = list(qubits)
    n = int(math.log2(len(state)))
    probs = probabilities(state)

    # Probabilities being laid out in a x dimension cube
    dimensional_matrix = probs.reshape([2] * n)

    # The qubits we are NOT looking for are sorted out here
    others = tuple(q for q in range(n) if q not in qubits)

    # Sum of the probabilities we want, sorted in the correct order
    marg = dimensional_matrix.sum(axis=others)
    order = sorted(qubits)
    marg = marg.transpose([order.index(q) for q in qubits])

    # Returning the marginal probabilities from a cube to a one dimensional array
    return marg.reshape(-1)



