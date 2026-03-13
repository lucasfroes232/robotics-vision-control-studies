import numpy as np
from spatialmath.base import rot2
from sympy import Symbol, Matrix, simplify

print("--- Teste Numérico ---")
R = rot2(0.3)
print("Matriz R:\n", R)

print("\nDeterminante de R:", np.linalg.det(R))
print("Determinante de R @ R:", np.linalg.det(R @ R))

print("\n--- Teste Simbólico ---")
theta = Symbol('theta')
R_sym = Matrix(rot2(theta)) 

print("Matriz R Simbólica:")
print(R_sym)

R_squared = simplify(R_sym * R_sym)
print("\nMatriz R * R simplificada:")
print(R_squared)

det_simplificado = R_sym.det().simplify()
print(f"\nDeterminante simbólico simplificado: {det_simplificado}")