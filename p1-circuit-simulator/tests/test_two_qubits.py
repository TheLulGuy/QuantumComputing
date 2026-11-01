import numpy as np
from qsim.gates import CNOT, H
from qsim.state import zero_state, apply_gate_fast, apply_gate_all, apply_gate_fast_specific
# CNOT gate tests
def test_cnot_10_to_11():
    s = np.array([0, 0, 1, 0], dtype=complex)
    expected = np.array([0, 0, 0, 1], dtype=complex)
    assert np.allclose(CNOT @ s, expected)

def test_cnot_keeps_first_qubit():
    s = np.array([1, 1, 0, 0], dtype=complex)
    assert np.allclose(CNOT @ s, s)

def test_cnot_bell_state():
    s = zero_state(2)
    result = apply_gate_fast_specific(s, H, 0)
    result = apply_gate_fast_specific(result, CNOT, [0, 1])
    expected = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    assert np.allclose(result, expected)