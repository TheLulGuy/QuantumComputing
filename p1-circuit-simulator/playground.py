from qsim.state import *
from qsim.gates import *
from qsim.circuit import Circuit

c = Circuit(2).h(0).cx(0, 1)
print(c.run())