import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
from numpy.linalg import norm

def hw2_isom():
    R = 8.314 # [J/K/mol]

    # A = nC4H10, B = iC4H10, C = C5H12
    xi0 = np.array([.9, 0, .1]) # [A, B, C]
    cAi = 9300 # [mol/m3]
    cs = cAi / xi0[0] # total concentration shall remain constant [mol/m3]
    # cBi = 0
    cCi = cs * xi0[2] # [mol/m3]
    n = 163e3 # feed rate [mol/h]
    x_target = 0.70 # target conversion


    # stoichiometry of reaction - conversion functions
    cA = lambda x: cAi*(1-x)
    cB = lambda x: x*cAi
    cC = lambda x: cCi

    Ea = 65.7e3 # [J/mol]
    Tk0 = 360 # [K]
    k0 = 31.1 # [h-1]
    k = lambda T: k0 * np.exp(-Ea/R * (1/T - 1/Tk0)) # forward reaction rate constant [h-1]

    Cpi = np.array([141, 141, 161]) # component Cp [J/K/mol]
    Cp = np.sum(Cpi*xi0) # total Cp shall remain constant since Cpi(1) = Cpi(2)
    DHr = -6900 # [J/mol]
    # I could caculate DHr = f(T), but Cpi(1) - Cpi(2) is evidently 0 therefore DHr = const

    K0 = 3.03
    TK0 = 273.15 + 60 # [K]
    K = lambda T: K0 * np.exp(-DHr/R * (1/T - 1/TK0)) # equilibrium constant
    kR = lambda T: k(T) / K(T) # backward reaction rate constant [h-1]

    r = lambda T,x: k(T)*cA(x) - kR(T)*cB(x) # reaction rate [mol/m3/h]

    Ti = 330 # initial temperature [K]
    DTad = lambda x: -DHr / Cp * cAi/cs * x # adiabatic deltaT

    print('ADIABATIC EQUILIBRIUM')
    # root callback to calculate adiabatic equilibrium    
    def modelAdiaEq(u):
        x, T = u
        return (
            r(T,x),
            T - Ti - DTad(x),
            )

    sol = sp.optimize.root(modelAdiaEq, (x_target, Ti+DTad(x_target)))
    x_eq, T_eq = sol.x
    print('(fsolve resid = {:.2e})'.format(norm(sol.fun)))
    print('[x, T] = {:.1f}%, {:.1f}°C'.format(x_eq*100, T_eq - 273.15))


    print('\nCSTR')
    # root callback for CSTR calculation
    def modelCSTR(u):
        V, T = u
        return (
            n/cs * (cAi - cA(x_target)) - r(T,x_target) * V, # balance of nA
            n*Cp*(T-Ti) + DHr * r(T,x_target) * V, # balance of H
            )
    T_guess = Ti + DTad(x_target) # temp estimate via adiabatic deltaT [K]
    V_guess = n / cs / k(T_guess) # volume estimate merely by dimensional analysis [m3]
    sol = sp.optimize.root(modelCSTR, (V_guess, T_guess))
    V, T = sol.x
    print('(fsolve resid = {:.2e})'.format(norm(sol.fun)))
    print('V = {:.2f} m3'.format(V))
    print('T = {:.1f}°C'.format(T-273.15))


    print('\nPFR')
    
    # solve_ivp callback for PFR calculation
    def modelPFR(_, u):
        x, T = u
        return (
            r(T,x) / n * cs/cAi, # differential balance of nA
            - DHr * r(T,x) / (n * Cp), # differential balance of H
            )
    # event to stop solve_ivp
    def stop_when_reacted(_, u):
        return u[0] - x_target
    stop_when_reacted.terminal = True
    stop_when_reacted.direction = 1

    u0 = [0, Ti] # [x, T]
    V_span = (0, V*10)
    sol = sp.integrate.solve_ivp(modelPFR, V_span, u0, method='RK45', events=stop_when_reacted, max_step=1e-3)
    V = sol.t
    x = sol.y[0, :] * 100
    T = sol.y[1, :] - 273.15
    print('V    = {:.2f} m3'.format(np.max(V)))
    print('Tout = {:.1f}°C'.format(np.max(T)))
    
    fig, ax = plt.subplots()
    ax.plot(V, x, 'k-')
    ax.plot([0, np.max(V)], [x_eq*100, x_eq*100], 'k:')
    ax.set_xlim(0)
    ax.set_ylim(0, 100)
    ax2 = ax.twinx()
    ax2.plot(V, T, 'r-')
    ax2.set_ylim(50, 100)
    ax.set_xlabel('V [m3]')
    ax.set_ylabel('x [%]', color='k')
    ax2.set_ylabel('T [°C]', color='r')
    plt.title('PFR')
    plt.show()


hw2_isom()
