import numpy as np

# ── Qubit states ──────────────────────────
ket_0 = np.array([1, 0], dtype=complex)   # |0⟩
ket_1 = np.array([0, 1], dtype=complex)   # |1⟩

# ── Hadamard gate ─────────────────────────
H = np.array([[1,  1],
              [1, -1]], dtype=complex) / np.sqrt(2)

# ── Apply H to |0⟩ ────────────────────────
result = H @ ket_1

print("H|0⟩ =", result)
print("Probabilities:", np.abs(result)**2)
print("Sum of probabilities:", round(sum(np.abs(result)**2), 4))