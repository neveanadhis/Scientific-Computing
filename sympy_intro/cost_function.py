from sympy import symbols, solve, diff
#Define the variable
x = symbols('x')

#Define the cost function
C = 5*x**3-10*x**2+4*x+3

#Compute derivative
C_prime = diff(C, x)
print(f'The first derivative is: {C_prime}')

#Find critical points
critical_points = solve(C_prime, x)
print(f'The critical points are: {critical_points}')

#Compute second derivative
C_double_prime = diff(C_prime, x)

for point in critical_points:
    second_derivative_value = C_double_prime.subs(x, point)


#Interpret results
if second_derivative_value > 0:
    print(f'At point {point} the cost is minimized')
else:
    print(f'At point {point} the cost is maximized')

