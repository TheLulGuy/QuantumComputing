import time
import tracemalloc

from qsim.state import apply_gate_specific, apply_gate_fast_specific, zero_state
from qsim.gates import X


def time_it(func, state, repeats=1):
    """Smallest time over `repeats` runs, in seconds."""
    best = float("inf")
    for _ in range(repeats):
        t = time.perf_counter()
        func(state, X, 5)
        best = min(best, time.perf_counter() - t)
    return best


def peak_memory_mb(func, state):
    """Peak extra memory used by one call, in megabytes."""
    tracemalloc.start()
    try:
        func(state, X, 5)
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return peak / 1e6


print("Benchmark for the Kronecker method")
print("qubits  seconds   peak MB")
for item in range(3):
    n = 12 + item
    state = zero_state(n)
    try:
        seconds = time_it(apply_gate_specific, state)
        mb = peak_memory_mb(apply_gate_specific, state)
        print(f"{n:<7} {seconds:<9.4f} {mb:.1f}")
    except MemoryError:
        print(f"{n:<7} ran out of memory (expected)")
        time.sleep(1)

print()
print("Benchmark for the fast method")
print("qubits  seconds     peak MB")
for item in range(20):
    n = 12 + item
    state = zero_state(n)
    seconds = time_it(apply_gate_fast_specific, state, repeats=5)
    mb = peak_memory_mb(apply_gate_fast_specific, state)
    print(f"{n:<7} {seconds:<11.6f} {mb:.2f}")