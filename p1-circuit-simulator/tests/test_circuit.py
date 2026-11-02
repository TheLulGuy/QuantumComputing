from qsim.circuit import Circuit
import numpy as np

def test_circuit_bell_state():
    state = Circuit(2).h(0).cx(0, 1).run()
    expected = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    assert np.allclose(state, expected)