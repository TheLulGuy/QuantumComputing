## Projects related to Quantum Computing

Features projects related to quantum computing, covering the fundamentals necessary for quantum computing

### Progress so far

- Added the following gates
  - H
  - X
  - Z

Circuit applies Kronicker factor to calculate gates for
- All qubits
- Specific qubits

Circuit also uses fast factor method to calculate gates for
- All qubits
- Specific qubits 

Benchmark for the Kronecker method
qubits  seconds   peak MB
12      0.1833    335.8
13      0.7013    1342.4
14      ran out of memory (expected)

Benchmark for the fast method
qubits  seconds     peak MB
12      0.000037    0.13
13      0.000036    0.26
14      0.000193    0.53
15      0.000546    1.05
16      0.000767    2.10
17      0.001240    4.20
18      0.002053    8.39
19      0.004727    16.78
20      0.010391    33.56
21      0.021196    67.11