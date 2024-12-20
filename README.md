# VQE
A Variational Quantum Eigensolver

This Variational Quantum Eigensolver solves for the ground state energy of a molecule by considering the taking the molecular geometry of the molecule and the hamiltonian as its two main inputs. It then approximates an intial anstaz to then run through a classical parameterized circuit to produce the ground state energy of a molecule. Traditionally, this would be very complex for _extremely_ large molecules, such as the ones used in material science, but with the advent of quantum computers in chemsitry, we can theoretically solve for any molecule (provided you have the molecular geometry).

The Psi4 driver does not natively support Windows. A conda environment is recommended!
Also, the code provided is designed to simulate a quantum computer via Qiskit. I have built a seperate version where the algorithm is executed on a real quantum computer via IBM's qiskit_runtime_service.
