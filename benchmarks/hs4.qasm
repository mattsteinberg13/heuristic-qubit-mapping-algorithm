version 1.0

qubits 4

h q[0]
h q[1]
h q[2]
h q[3]

x q[0]
x q[2]

h q[1]
h q[3]

cnot q[0],q[1]
cnot q[2],q[3]

h q[1]
h q[3]

x q[0]
x q[2]

h q[0]
h q[1]
h q[2]
h q[3]

h q[1]
h q[3]

cnot q[0],q[1]
cnot q[2],q[3]

h q[1]
h q[3]

h q[0]
h q[1]
h q[2]
h q[3]

measure q[0]
measure q[1]
measure q[2]
measure q[3]