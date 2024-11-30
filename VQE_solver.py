from qiskit_nature.second_q.drivers import Psi4Driver

# Define the driver for the hydrogen molecule
driver = Psi4Driver(
    config="""
molecule h2o {
    0 1
    O 0.0 0.0 0.0
    H 0.0 0.757 0.586
    H 0.0 -0.757 0.586
    no_com
    no_reorient
}

set {
  basis sto-3g
  scf_type pk
  reference rhf
}

"""
)

# Run the electronic structure problem
es_problem = driver.run()

from qiskit_nature.second_q.mappers import JordanWignerMapper
mapper = JordanWignerMapper()

# Import the classical eigensolver as an alternative to VQE
from qiskit_algorithms import NumPyMinimumEigensolver

# Use NumPyMinimumEigensolver to obtain an exact solution
solver = NumPyMinimumEigensolver()

from qiskit_nature.second_q.algorithms import GroundStateEigensolver

# Set up the ground state eigensolver
calc = GroundStateEigensolver(mapper, solver)

# Execute the solver
result = calc.solve(es_problem)

# Print the ground state energy result
print("Ground State Energy:", result.groundenergy)

