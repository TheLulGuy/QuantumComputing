from qsim.state import apply_gate_specific, zero_state
from qsim.gates import X

import time
for item in range(3):
    a = 12 + item
    t = time.time()
    apply_gate_specific(zero_state(a), X, 5)
    print(a, time.time() - t)