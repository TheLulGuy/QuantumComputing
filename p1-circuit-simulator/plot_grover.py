from qsim.measure import probabilities
from qsim.algorithms import grover, grover_circuit, optimal_iterations
import numpy as np
import matplotlib.pyplot as plt

# Control
marked = 6
n = 4
k = [item for item in range(0, 11)]
# if you want to see different values, uncomment this and changed marked and n variables
# k = [item for item in range(0, 2**(n//2 + 1))]
probs = []
for item in k:
    state = grover_circuit(marked, n, iterations=item).run()
    probs.append(probabilities(state)[marked])

best_k = optimal_iterations(n)
print(probs)
plt.plot(k, probs, marker='o')
plt.title(f'Grover plo n={n} marked={marked}')
plt.xlabel('Number of iterations(upto 10)')
plt.ylabel('Probability of getting the marked state')
plt.axvline(best_k, linestyle='--')
plt.savefig('./results_grover_plot/grover_success.png')
plt.show()