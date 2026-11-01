from qsim.state import *
from qsim.gates import *

a = np.array([0, 1, 0, 0], dtype=complex)
print(apply_gate_fast_specific(a, Z, 1))