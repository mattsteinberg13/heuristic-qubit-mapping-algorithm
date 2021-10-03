version 1.0 

qubits 4

x q[0]
x q[1]
h q[3]

cnot q[2],q[3]

t q[0]
t q[1]
t q[2]
tdag q[3]

cnot q[0],q[1]
cnot q[2],q[3]
cnot q[3],q[0]
cnot q[1],q[2]
cnot q[0],q[1]
cnot q[2],q[3]

tdag q[0]
tdag q[1]
tdag q[2]
t q[3]

cnot q[0],q[1]
cnot q[2],q[3]

s q[3]

cnot q[3],q[0]

h q[3]

measure q[0]
measure q[1]
measure q[2]
measure q[3]