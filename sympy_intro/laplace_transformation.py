from sympy import symbols, factor, apart, inverse_laplace_transform, expand, solve
from sympy.abc import s, t

#Define H(s)
H = 1 / (s**2 + 3*s + 2)

#Factor the denominator
factored_denominator = factor(s**2 + 3*s + 2)
print(f"Factored denominator: {factored_denominator}")

#Compute inverse Laplace transform
h_t = inverse_laplace_transform(H, s, t)
print(f"Inverse Laplace Transform: {h_t}")

#Find the poles
poles = solve(s**2 + 3*s + 2)
print(f"Poles of the system: {poles}")

