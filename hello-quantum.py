# My first Python program
# Quantum Computing Research - Python Practice

name = "Quantum Researcher"
greeting = "Hello from Python!"

print(greeting)
print("Welcome,", name)

# A qubit state: alpha|0⟩ + beta|1⟩
alpha = 0.6
beta = 0.8

print("Qubit amplitudes:", alpha, beta)
print("Normalised?", round(alpha**2 + beta**2, 4) == 1.0)