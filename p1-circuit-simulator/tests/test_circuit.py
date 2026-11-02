from qsim.circuit import Circuit
import numpy as np
import pytest

def test_circuit_bell_state():
    state = Circuit(2).h(0).cx(0, 1).run()
    expected = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    assert np.allclose(state, expected)

def test_gate_count_and_depth():
    c = Circuit(2).h(0).h(1).cx(0, 1)
    assert c.gate_count() == 3
    assert c.depth() == 2

def test_depth_waits_for_busiest_qubit():
    c = Circuit(2).h(0).h(0).h(0).cx(0, 1).h(1)
    assert c.depth() == 5

def test_bad_target_raises():
    with pytest.raises(TypeError):
        Circuit(2).y([0, 1])