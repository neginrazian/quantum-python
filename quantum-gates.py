import numpy as np
#Qutbi States 
ket_0=np.array([1,0],dtype=complex)
ket_1=np.array([0,1],dtype=complex)
#Gates
H = np.array([[1,1],
              [1,-1]],dtype=complex)/np.sqrt(2) #Hadamard
X = np.array([[0,1],
              [1,0]],dtype=complex) #Pauli-X
Z = np.array([[1,0],
              [0,-1]],dtype=complex)

# Helper function
def apply(gate, state):
    """Apply a gate to a qubit state and print the result."""
    result=gate@state
    probs=np.abs(result)**2
    print(f" state:{result.round(3)}")
    print(f"P(|0⟩)={probs[0]:.2f} P(|1⟩)={probs[1]:.2f}")
    return result

# Experiment
print("--- X|0⟩ (NOT gate on |0⟩) ---")
state = apply(X,ket_0)

print("--- H|0⟩ (NOT gate on |0⟩) ---")
state = apply(H,ket_0)

print("--- H then X (sequence of gates) ---")
state1 = apply(H,ket_0)
state1 = apply(X,state1)

state2 = apply(X@H,ket_0)

print("--- Z|1⟩ (Pauli-Z on |1⟩) ---")
state = apply(Z, ket_1)