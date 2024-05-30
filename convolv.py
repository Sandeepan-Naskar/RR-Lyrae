import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

def g(tau, sigma, lambda_, a0, a1, phi, w):
    # w = 1
    T = 2*np.pi/w #in hours
    t = sy.Symbol('t')
    # print("haha")
    return a0 + a1*sy.integrate(sy.exp(-lambda_ * t) * sy.exp(t-(tau+phi)%T)**2/(2*sigma*sigma), (t, 0, 1))
y = []
# for tau in np.linspace(-5, 5, 100):
#     y.append(g(tau, 1, 1, 0, 1, 0, 2).evalf())
#     print(y[-1])

# plt.plot(y)
# plt.savefig('test.png')
# plt.close()

def per_gaus(x, a0, a1, phi, k):
    w = 2*np.pi/1
    return a0 + a1*np.exp(k*np.cos(w*x + phi))/(1 + k**2/4 + k**4/64 + k**6/2304 + k**8/147456)

plt.plot(np.linspace(-5, 5, 100), per_gaus(np.linspace(-5, 5, 100), 0, 1, 0, 1))
plt.savefig('test.png')
plt.close()
