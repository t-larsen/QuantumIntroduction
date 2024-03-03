# Inspired from:
# Ref.: https://docs.quantum.ibm.com/api/qiskit/qiskit.visualization.plot_histogram

# Import Qiskit
from qiskit import QuantumCircuit
from qiskit import Aer, transpile
from qiskit.tools.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi
import numpy as np
import os

# Input values
shots = 10000
result_path = "Lectures/#3/simulate_state_shots/results/"
initial_state = [3./5., 4./5.]

# Create circuit
circuit = QuantumCircuit(1)
circuit.initialize(initial_state, 0)
circuit.draw('mpl', filename=os.path.join(result_path, "initial_state.png"))
circuit.measure_all()

# Transpile for simulator and run and get counts
simulator = Aer.get_backend('aer_simulator')
circuit = transpile(circuit, simulator)
result = simulator.run(circuit, shots=shots, memory=True).result()
memory = result.get_memory(circuit)

# Post processing
counts = result.get_counts(circuit)
plot_histogram(counts, legend=None, color=['crimson'], title="Histogram", \
    filename=os.path.join(result_path, "histogram_counts.png"))

filename = os.path.join(result_path, "results.txt")
with open(file=filename, mode="wt") as file:
    # Redirecting print output to the file
    print(f"---------------------------------------", file=file)
    print(f"Theory, Pr(state '0')     >>>    {(np.abs(initial_state[0])**2):.4f}", file=file)
    print(f"Theory, Pr(state '1')     >>>    {(np.abs(initial_state[1])**2):.4f}", file=file)
    print(f"Measured, Pr(state '0')   >>>    {(counts['0']/(counts['0']+counts['1'])):.4f}", file=file)
    print(f"Measured, Pr(state '1')   >>>    {(counts['1']/(counts['0']+counts['1'])):.4f}", file=file)
    print(f"---------------------------------------", file=file)  

if len(memory) < 101:
    print(memory)