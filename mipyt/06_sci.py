import numpy as np
from scipy import constants # it has all kinds of universal constants and UNIT CONVERSIONS woot!

from numpy.linalg import solve
from scipy.linalg import solve as solve2

from scipy.optimize import root, brentq, minimize, fsolve, curve_fit
from scipy.interpolate import UnivariateSpline
from scipy.integrate import quad, solve_ivp

from matplotlib import pyplot as plt

V = 17.3 # m3
V/constants.liter # convert SI (m3) to liter
constants.kilo # = 1000



# ~A\b SOLVING MATRICES - with NUMPY ctuly
A = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x1 = solve(A, b)
x2 = solve2(A, b)
print(f"solving a matrix, x = {x1}")
print(f"solution is same from NumPy and SciPy? {(x1 == x2).all()}\n")



# ~FZERO
eqn = lambda x: x + np.cos(x)

sol = root(eqn, 0) # with initial estimate 0
print(f"x+cos(x) solved with root: {sol.x}") # sol is object with some gimmicks

sol = brentq(eqn, -1, 1) # with bounds a, b
print(f"x+cos(x) solved with brentq: {sol}\n") # sol is the root
# sol = brentq(eqn, 0, 1) # ValueError because f(a)*f(b) > 0



# ~FSOLVE
def eqns(p): # intended for tuple, but also works for list this way (both are unpackable)
    x, y = p # unpack tuple
    return (x+y**2-4, np.exp(x) + x*y - 3) # residuals

sol = root(eqns, (1, 1)) # for initial estimate I could write np.ones(7) if there is a lot of them
# (tuples, lists, np.arrays) work as well
print(f"set of eqns solved with root: {sol.x}")
print(f"residuals: {eqns(sol.x)}\n")



# ~FMINCON
eqn = lambda x: x*x + x + 2
sol = minimize(eqn, 0) # find minimum with initial estimate
print(f"x^2+x+2 solved with minimize: {sol.x}\n") # sol is the root



# QUAD
fn = lambda x: np.sin(x)
X, err = quad(fn, 0, np.pi) # the error is an estimate
print(f"integral of sin(x) from 0 to pi: {X}, analytical: {-np.cos(np.pi)--np.cos(0)}\n")



# ODE
dcA = lambda t, cA: -0.02*cA
t_span = (0, 1000)
cA0 = [33]
sol = solve_ivp(dcA, t_span, cA0, method='RK45') # default method is RK45, but it also has implicit methods for stiff odes
plt.plot(sol.t, sol.y[0, :], 'g-')
plt.xlabel('t')
plt.ylabel('cA')
plt.title('ode45')
plt.show()



# SPLINE INTERPOL
x = np.linspace(2, 17, num=7)
y = x**2 + 50*np.sin(x) + 1.2

spline_fn = UnivariateSpline(x, y)
xs = np.linspace(np.min(x), np.max(x), num=100)
ys = spline_fn(xs)

plt.plot(x, y, 'kx')
plt.plot(xs, ys, 'g-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Splajn')
plt.show()



# ~LSQCURVEFIT
fn = lambda x, a, b, c: a + b*x + c*x*x # the parametrized function we want to fit

xdata = np.linspace(0, 6, num=50)
ydata = fn(xdata, 2.3, 1.3, 0.9) * ( .8 + 0.4*np.random.random(xdata.shape)) # generate noisy ydata
params, covariance = curve_fit(fn, xdata, ydata, p0=np.ones(3)) # covariance matrix might be useful..
print(f"least squares fitted a,b,c: {params}")

xs = np.linspace(np.min(xdata), np.max(xdata), num=100)
ys = fn(xs, *params)
plt.plot(xdata, ydata, 'kx')
plt.plot(xs, ys, 'g-')
plt.title('Curve fit')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# WHAT ELSE CAN SCIPY DO?
# - solve_bvp HOLY SH*T!!!
# - lsq_linear for linear regression, but I can do it myself using matrix solving..
# - graph algorithms such as Dijkstra or triangulation from points
# - can also work with sparse data
# - significance tests
# - it also has interoperability with matlab arrays, lolwut?
