from qsim.state import *
from qsim.gates import *

s = zero_state(2)

print(apply_gate_fast_specific(s, H, 0))