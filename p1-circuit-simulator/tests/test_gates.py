import numpy as np
from qsim.state import zero_state, apply_1q
from qsim.gates import H

def test_h_on_zero_gives_equal_amplitudes():
    s = apply_1q(zero_state(1), H)
    expected = np.array([1, 1]) / np.sqrt(2)
    assert np.allclose(s, expected)

def test_h_twice_returns_to_zero():
    s = apply_1q(apply_1q(zero_state(1), H), H)
    assert np.allclose(s, zero_state(1))