import numpy as np

H = np.array([
    [1, 1],
    [1, -1]
], dtype=complex) / np.sqrt(2)

# Not gate
X = np.array([
    [0, 1],
    [1, 0]
], dtype=complex)

# Flips the qubit by pi radians, basically making the amplitudes negative 
Z = np.array([
    [1, 0],
    [0, -1]
], dtype=complex)