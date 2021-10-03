version 1.0

qubits 8

x q[7]

h q[0]
h q[1]
h q[2]
h q[3]
h q[4]
h q[5]
h q[6]
h q[7]

cnot q[0],q[7]
cnot q[1],q[7]
cnot q[2],q[7]

h q[0]
h q[1]
h q[2]
h q[3]
h q[4]
h q[5]
h q[6]
h q[7]

measure q[0]
measure q[1]
measure q[2]
measure q[3]
measure q[4]
measure q[5]
measure q[6]
measure q[7]