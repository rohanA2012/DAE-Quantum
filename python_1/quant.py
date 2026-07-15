import qiskit as q

qc = q.QuantumCircuit(1)

qc.h(0)
qc.measure_all()
print(qc)
