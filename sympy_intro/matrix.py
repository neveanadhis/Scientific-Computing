from sympy import Matrix, symbols, solve, simplify
#Define matrix
A = Matrix([[2,1], [1,3]])

#Compute determinant
det_A = A.det()
print(f'Determinant of A is: {det_A}')

#Compute eigenvalues
eigenvalues = A.eigenvals()
print(f'Eigenvalues of A are: {list(eigenvalues.keys())}')


#Define the eigenvalue symbol l
l = symbols('l')

#Define the characteristic equation
char_eq = A.charpoly(l).as_expr()
print(f'Characteristic equation is: {char_eq} = 0')

#Verification
verification = [simplify(char_eq.subs(l, eig)) == 0 for eig in eigenvalues.keys()]
print(f'Verification: {verification}')
