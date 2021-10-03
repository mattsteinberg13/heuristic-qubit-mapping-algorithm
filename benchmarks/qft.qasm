verison 1.0

qubits 2

h q[1]

tdag q[1]

cnot q[0],q[1]

tdag q[1]

cnot q[0],q[1]

s q[1]
t q[0]
h q[0]

cnot q[1],q[0]

cnot q[0],q[1]

cnot q[1],q[0]

h q[1]
h q[0]

measure q[0]
measure q[1]