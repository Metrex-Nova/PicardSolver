import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate, exp, lambdify

tol = 1e-2
trange = (0, 2)
numpoints = 100

t = symbols('t')
s = symbols('s')
uprev = 1  # initial approximation u0(t) = 1

tvalues = np.linspace(trange[0], trange[1], numpoints)
iterates = [np.full_like(tvalues, uprev)]  # store numeric values of iterates

print("Picard Iterates for u' = u, u(0) = 1")
print("=" * 50)
print(f"{'t':>8} {'u0(t)':>10}")

exact = np.exp(tvalues)  # exact solution e^t

n = 0
maxerror = float('inf')

while maxerror > tol:
    n += 1
    # Prepare integrand
    if isinstance(uprev, (int, float)):
        integrand = uprev
    else:
        integrand = uprev.subs(t, s)

    try:
        integral = integrate(integrand, (s, 0, t))
        ucurrent = 1 + integral  # Picard iteration formula

        # Numerical evaluation for error calculation
        if hasattr(ucurrent, 'subs'):
            ufunc = lambdify(t, ucurrent, 'numpy')
            currentvalues = ufunc(tvalues)
        else:
            currentvalues = np.full_like(tvalues, ucurrent)

        iterates.append(currentvalues)

        maxerror = np.max(np.abs(currentvalues - exact))
        print(f"n={n} u{n}(t) = {ucurrent}")
        print(f"Max error: {maxerror:.6f}")

        if maxerror <= tol:
            print(f"Tolerance {tol} achieved at iteration n={n}")
            print(f"Maximum error: {maxerror:.6f}")
            break

        uprev = ucurrent

    except Exception as e:
        print(f"Error in iteration {n}: {e}")
        break

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(tvalues, exact, 'k-', linewidth=2, label='Exact e^t')

colors = ['r', 'g', 'b', 'm', 'c']
for i, iterate in enumerate(iterates):
    if i < len(colors):
        plt.plot(tvalues, iterate, '--', color=colors[i], linewidth=1.5, label=f'Iterate {i}')
    else:
        plt.plot(tvalues, iterate, '--', linewidth=1, label=f'Iterate {i}')

plt.xlabel('t')
plt.ylabel('u(t)')
plt.title('Picard Iteration for u\' = u, u(0) = 1')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Final iteration: n = {n}")
print(f"Final maximum error: {maxerror:.6f}")
