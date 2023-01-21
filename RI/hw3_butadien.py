import numpy as np
import scipy as sp


def hw3_butadien():
    # constants
    p = 120e3  # [Pa]
    p_std = 101325  # [Pa]
    # T = 911  # [K]
    Kp = 1.27  # eq constant
    n0 = 13.88  # [mol/s]

    # _i means vector of values per compound [butadien, dimer, H2O]
    # all of the array functions work with X row vector, compounds are in column

    x0_i = np.array([[2], [0], [1]]) / 3  # initial molar frac
    n0_i = n0 * x0_i  # initial molar flow [mol/s]
    # note: n0_i[0] is key compound reference (butadien)

    mu_i = np.array([[-1], [0.5], [0]])  # reaction stoichiometry normalized to key compound (butadien)
    n_i = lambda X: n0_i + mu_i * n0_i[0] * X  # molar flows as function of conversion (X) [mol/s]
    p_i = lambda X: p * n_i(X) / np.sum(n_i(X), 0)  # partial pressures as function of conversion [Pa]

    # reaction rate [mol/m3/h]
    r = lambda pi: 15.9 * ((pi[0, :] / p_std)**2 - 1 / Kp * pi[1, :] / p_std)

    X_eq = sp.optimize.brentq(lambda X: r(p_i(X)), 0, 1)  # equilibrium conversion
    print('X equil  = {:.1f}%:'.format(X_eq * 100))

    X_target = 0.95 * X_eq  # target butadien conversion

    dVdX = lambda X: n0_i[0] / r(p_i(X))  # derivation dV/dX [m3]
    V, _ = sp.integrate.quad(dVdX, 0, X_target)  # reactor volume [m3]

    print('X target = {:.1f}%:'.format(X_target * 100))
    print('V = {:.2f} m3'.format(V))


hw3_butadien()
