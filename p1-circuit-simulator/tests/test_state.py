import numpy as np
from qsim.state import zero_state

def test_zero_state():
    s = zero_state(3)
    # Check if 3 qubits have 8 states
    # and the first state is a 1
    assert len(s) == 8
    assert s[0] == 1

def test_zero_state_has_right_size():
    assert len(zero_state(3))

def test_zero_state_is_all_zeroes_except_first():
    s = zero_state(2)
    assert s[0] == 1
    assert np.allclose(s[1:], 0)


