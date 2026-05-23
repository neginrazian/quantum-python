import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
# Qubit State to Block coordinates
def state_to_bloch(state):
    alpha=state[0]
    beta = state[1]
    x = 2 * np.real(np.conj(alpha) * beta)
    y = 2 * np.imag(np.conj(alpha) * beta)
    z = np.abs(alpha)**2 - np.abs(beta)**2
    return x, y, z
# Rotation Gate
def Rx(theta):
    return np.array([[np.cos(theta/2),  -1j*np.sin(theta/2)],
                     [-1j*np.sin(theta/2),  np.cos(theta/2)]], dtype=complex)
# Initial State 
ket_0 = np.array([1,0],dtype=complex)

#Set up the Figure
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

# Drarw sphere surface 
u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 50)
sx = np.outer(np.cos(u), np.sin(v))
sy = np.outer(np.sin(u), np.sin(v))
sz = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(sx, sy, sz, color='lightblue', alpha=0.1)

# Draw axes 
ax.quiver(0,0,0, 0,0,1.3, color='gray', linewidth=0.8)
ax.quiver(0,0,0, 0,0,-1.3, color='gray', linewidth=0.8)

# Axis labels
ax.text(0, 0,  1.4, '|0⟩', fontsize=12, ha='center')
ax.text(0, 0, -1.4, '|1⟩', fontsize=12, ha='center')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_title('Bloch sphere — Rx rotation')

# ── Animation ─────────────────────────────────────────
angles = np.linspace(0, 2*np.pi, 120)
arrow = [None]

def update(frame):
    if arrow[0]:
        arrow[0].remove()
    theta = angles[frame]
    state = Rx(theta) @ ket_0
    x, y, z = state_to_bloch(state)
    arrow[0] = ax.quiver(0, 0, 0, x, y, z,
                         color='red', linewidth=2)
    ax.set_title(f'Rx(θ)  θ = {np.degrees(theta):.0f}°')

ani = FuncAnimation(fig, update, frames=120,
                    interval=50, repeat=True)

plt.show()