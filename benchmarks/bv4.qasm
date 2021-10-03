version 1.0

qubits 4

x q[3]

h q[0]
h q[1]
h q[2]
h q[3]

cnot q[0],q[3]
cnot q[1],q[3]
cnot q[2],q[3]

h q[0]
h q[1]
h q[2]
h q[3]

measure q[0]
measure q[1]
measure q[2]
measure q[3]