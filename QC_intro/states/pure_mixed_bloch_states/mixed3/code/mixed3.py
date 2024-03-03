#
# https://docs.quantum.ibm.com/api/qiskit/0.19/qiskit.visualization.plot_bloch_multivector
#

from qiskit import QuantumCircuit, BasicAer, execute
#from qiskit.visualization import plot_bloch_multivector, plot_state_city, plot_state_qsphere
from qiskit import visualization

 
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
 
backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc, backend).result()
#print(job)

# Plots
visualization.plot_bloch_multivector(job.get_statevector(qc)) \
  .savefig("QC_intro/states/pure_mixed_bloch_states/mixed3/results//mixed_bloch_3XL.png")
visualization.plot_state_city(job.get_statevector(qc), color=['midnightblue', 'midnightblue']) \
  .savefig("QC_intro/states/pure_mixed_bloch_states/mixed3/results//mixed_city_3XL.png")
visualization.plot_state_qsphere(job.get_statevector(qc)) \
  .savefig("QC_intro/states/pure_mixed_bloch_states/mixed3/results/state_qsphere_3XL.png")


