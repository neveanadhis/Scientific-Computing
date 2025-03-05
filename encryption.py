from sympy import symbols, Mod, mod_inverse
#Define the variables
P, e, N = symbols('P e N')

#Define the  encyrption function
C = Mod(P**e, N)
print(f'The symbolic encryption function is: {C}')

#Given values
P_value = 7
e_value = 3
N_value = 33

#Compute the modular inverse of P
P_inv = mod_inverse(P_value, N_value)
print(f'The modular inverse of P is: {P_inv}')

#Compute C
C_value = pow(P_value, e_value, N_value)
print(f'The Ciphertext is: {C_value}')


