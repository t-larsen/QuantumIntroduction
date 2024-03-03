# Bell state

import numpy as np

n_qubits = 3
II = np.identity(n_qubits)
RR = np.random.randn(n_qubits, n_qubits)
print(RR)

print(II[1,:])

for k in range(n_qubits):
    print(k, np.matmul(RR, II[:,k]))
  