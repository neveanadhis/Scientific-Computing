from sympy import symbols, solve, diff
#define variable
x = symbols('x')

#define the function
L = 3*x**2+2*x-5

#Compute first derivative
L_prime = diff(L, x)
print(f'Gradient is: {L_prime}')

#compute optimal solution
optimal_solution = solve(L_prime, x)
print(f'Optimal solution is: {optimal_solution}')

#find second derivative
L_double_prime = diff(L_prime, x)
print(f'Second derivative is: {L_double_prime}')

#Check if maximum or minimum point
point = L_double_prime.subs(x, optimal_solution[0])
if point < 0:
    print("It is a maximum point")
elif point > 0:
    print("It is a minimum point")
else:
    print("Inconclusive")
    
