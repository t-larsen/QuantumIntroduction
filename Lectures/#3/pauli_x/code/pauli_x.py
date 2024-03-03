#

# Import tools
from qiskit import QuantumCircuit, Aer, execute

# Input values
result_path = "Lectures/#3/pauli_x/results/"

# Create a quantum circuit with one qubit
circuit = QuantumCircuit(1)
initial_state = [0, 1]   # [3./5., 4./5.]  # [1/np.sqrt(2), 1/np.sqrt(2)]
circuit.initialize(initial_state, 0)
circuit.x(0)  # Apply to qubit 0

# Simulate the circuit
simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, simulator).result()

# Get the final state vector
state_vector = result.get_statevector()
print("Final state vector:", initial_state, state_vector)