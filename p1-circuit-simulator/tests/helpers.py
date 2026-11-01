import numpy as np

def random_state(n):
    rng = np.random.default_rng(n)
    state = rng.normal(size=2**n) + 1j * rng.normal(size=2**n)
    state = state / np.linalg.norm(state)
    return state

def basis(bits):
    state = np.zeros(2**len(bits), dtype=complex)
    bits = reversed(bits)
    final_index = 0
    for index, bit in enumerate(bits):
        bit = int(bit)
        final_index += bit * (2 ** index)

    state[final_index] = 1
    return state

    '''
    00 - 0 - 2^0
    01 - 1 - 2^1
    10 - 2 - 2 ^ 2
    11 - 3 - 2 ^ 2 + 2 ^ 1
    100 - 4
    101 - 2 ** 2 + 2 ** 0
    '''