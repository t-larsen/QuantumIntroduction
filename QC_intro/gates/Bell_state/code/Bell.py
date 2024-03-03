# Bell state

# Import relevant modules
from qiskit import *
from random import randint
import numpy as np

# Create a Quantum Circuit acting on a quantum 2-qubit register
n_qubits = 2
Q_circuit = QuantumCircuit(2)

# Add a H gate on qubit $q_{0}$, putting this qubit in superposition.
Q_circuit.h(0)

# Add a CX (CNOT) gate on control qubit $q_{0}$ and target qubit $q_{1}$, putting
# the qubits in a Bell state.
Q_circuit.cx(0, 1)

# Draw the Bell state circuit
Q_circuit.draw('mpl', filename="examples/Bell_state/results/Bell_Q-circuit")

# Import Aer
from qiskit import Aer

# Run the quantum circuit on a statevector simulator backend
backend = Aer.get_backend('statevector_simulator')

# Create a Quantum Program for execution
job = backend.run(Q_circuit)

result = job.result()
outputstate = result.get_statevector(Q_circuit, decimals=2)
print(outputstate)

from qiskit.visualization import plot_state_city
plot_state_city(outputstate, filename="examples/Bell_state/results/Bell_density")

size = 2**n_qubits
state_vectors = [np.identity(size)[i] for i in range(size)]


import qiskit.quantum_info as qi
c_matrix = qi.Operator(Q_circuit).data
print(c_matrix*state_vectors[0])
