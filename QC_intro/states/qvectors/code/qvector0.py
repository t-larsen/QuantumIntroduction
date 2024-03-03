#
# https://github.com/Qiskit/textbook/blob/main/notebooks/ch-states/representing-qubit-states.ipynb
#

from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector, plot_bloch_multivector
from math import sqrt, pi
 
Qcircuit = QuantumCircuit(1) # Create a quantum circuit with one qubit

# Define initial_state as |1>
initial_state = [0, 1]

# Apply initialisation operation to the 0th qubit
Qcircuit.initialize(initial_state, 0)

# Let's view our circuit
Qcircuit.draw('mpl', filename = "QC_intro/states/qvectors/results/vector_state_0")


# Tell Qiskit how to simulate our circuit
sim = Aer.get_backend('aer_simulator')


# Tell simulator to save statevector
Qcircuit.save_statevector()
# Create a Qobj from the circuit for the simulator to run
qobj = assemble(Qcircuit)
# Do the simulation and return the result
result = sim.run(qobj).result() 

# Display the output state vector
out_state = result.get_statevector()
print(out_state)



# 
# 
# 
#from qiskit_textbook.widgets import plot_bloch_vector_spherical
# [Theta, Phi, Radius]
#coords = [pi/2, 0, 1]
# Bloch Vector with spherical coordinates
#plot_bloch_vector_spherical(coords, 'mpl', filename = "slides/qvectors/results/bloch0")






