import pytest
from qsim.gates import *
from qsim.state import *

@pytest.mark.parametrize('n', [1, 2, 3, 4, 5])
@pytest.mark.parametrize('gate', [X, Z, H, Y])
def test_fast_matches_kron_specific(n, gate):
    rng = np.random.default_rng(n)
    state = rng.normal(size=2**n) + 1j * rng.normal(size=2**n)
    state = state / np.linalg.norm(state)
    for k in range(n):
        assert np.allclose(apply_gate_fast_specific(state, gate, k), apply_gate_specific(state, gate, k))

@pytest.mark.parametrize('n', [1, 2, 3, 4, 5])
@pytest.mark.parametrize('gate', [X, Z, H, Y])
def test_fast_matches_kron_all(n, gate):
    rng = np.random.default_rng(n)
    state = rng.normal(size=2**n) + 1j * rng.normal(size=2**n)
    state = state / np.linalg.norm(state)
    assert np.allclose(apply_gate_fast_all(state, gate), apply_gate_all(state, gate))
