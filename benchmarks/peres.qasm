version 1.0

qubits 3

x q[0]

x q[1]

t q[0]

t q[1]

h q[2]

cnot q[2],q[1]

tdag q[1]

cnot q[0],q[2]

cnot q[0],q[1]

tdag q[2]

cnot q[0],q[2]

t q[1]

t q[2]

cnot q[2],q[1]

tdag q[1]

h q[2]

measure q[0]
measure q[1]
measure q[2]