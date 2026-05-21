import numpy as np
import matplotlib.pyplot as plt
# Convert qubit state to Block sphere angles 
def state_to_boch(state):
    """"Convert a qubit state vector to Bloch sphere coordinates (x,y,z)."""
    alpha = state[0]
    beta = state[1]
    x = 2 * np.real(np.conj(alpha)*beta)
    y = 2 * np.imag(np.conj(alpha)*beta)
    z = np.abs(alpha)**2 - np.abs(beta)**2
    return x,y,z
# Draw the Bloch sphere
def draw_bloch(state, labels):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Draw the sphere
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    sx = np.outer(np.cos(u), np.sin(v))
    sy = np.outer(np.sin(u), np.sin(u))
    sz = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(sx, sy, sz, color='lightblue', alpha=0.1)

    #Draw axes
    ax.quiver(0,0,0, 0,0,1.3, color='gray', linewidth=0.8)
    ax.quiver(0,0,0, 0,0,-1.3, color='gray', linewidth=0.8)

     # Axis labels
    ax.text(0, 0,  1.4, '|0⟩', fontsize=12, ha='center')
    ax.text(0, 0, -1.4, '|1⟩', fontsize=12, ha='center')

    # Plot each state 
    colors = ['red', 'blue', 'green', 'orange']
    for i, (state, label) in enumerate(zip(state, labels)):
        x, y, z = state_to_boch(state)
        ax.quiver(0,0,0,x,y,z, color=colors[i], linewidth=2)
        ax.text(x*1.15, y*1.15, z*1.15, label, fontsize=10, color=colors[i])

    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])
    ax.set_title('Bloch Sphere')
    plt.tight_layout()
    plt.show()

# ── Gates ─────────────────────────────────────────────
H = np.array([[1,  1],
              [1, -1]], dtype=complex) / np.sqrt(2)
X = np.array([[0, 1],
              [1, 0]], dtype=complex)
Z = np.array([[ 1,  0],
              [ 0, -1]], dtype=complex)

# ── Qubit states to visualise ─────────────────────────
ket_0    = np.array([1, 0], dtype=complex)
after_H  = H @ ket_0
after_X  = X @ ket_0
after_XH = H @ X @ ket_0

states = [ket_0, after_H, after_X, after_XH]
labels = ["|0⟩", "H|0⟩", "X|0⟩", "HX|0⟩"]

draw_bloch(states, labels)