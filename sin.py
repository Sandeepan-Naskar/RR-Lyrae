
y_data = { 'z':[14.42023621,
                14.43234234,
                14.37424386,
                14.38389169,
                14.31336816,
                13.84435841,
                13.89632976,
                14.10817267,
                14.40599687],
            'i':[14.40948774,
                14.41838303,
                14.42701607,
                14.416151,
                13.78486548,
                13.7765156,
                13.96885395,
                14.13473115],
            'g':[14.71900401,
                14.70102038,
                14.77076003,
                14.84166644,
                14.24068659,
                13.57818949,
                13.61801554,
                13.92892945,
                14.30385407],
            'r':[14.48942824,
                14.50233509,
                14.50218182,
                14.51651103,
                14.19398228,
                13.6416802,
                13.71241158,
                13.88833264,
                14.1353249]
        }

x_data = {  'z':[61370.269,
                62278.228,
                62837.873,
                63739.645,
                66798.808,
                69397.953,
                72624.645,
                76368.681,
                79616.448],
            'i':[61548.311,
                62093.429,
                63018.404,
                63561.828,
                69214.707,
                72446.598,
                76185.505,
                79431.999],
            'g':[61728.434,
                62462.309,
                63198.348,
                63919.654,
                67171.513,
                68853.065,
                72085.937,
                75829.901,
                79801.654],
            'r':[61906.748,
                62644.857,
                63382.803,
                64106.345,
                66992.055,
                69030.443,
                72269.661,
                76008.017,
                79979.401]} 

x_data = {  'z': x_data['z'][:8], 'i': x_data['i'], 'g': x_data['g'], 'r': x_data['r'] }

y_data = { 'z':[14.40514758,
14.37345667,
14.42737395,
14.54901428,
14.32221192,
13.81009694,
13.85095909,
14.01395329

],      'i':[14.54519398,
14.50352498,
14.53218825,
14.5861154,
13.77732351,
13.8436201,
14.01792355,
14.04449866],

      'g':[14.76139049,
14.72870488,
14.8010871,
14.8181543,
14.24906006,
13.59374107,
13.70485201,
13.9467587,
14.42038599],

        'r':[14.56112607,
14.58646953,
14.59337058,
14.53696474,
14.21017661,
13.66615774,
13.71268766,
13.91492179,
14.1269]
}

y_error = { 'z':[
0.1470686281,
0.2322186311,
0.3655932942,
0.3231833737,
0.0987366488,
0.09882886481,
0.1125185095,
0.1117861893
            ],
            'i':[
0.2216144584,
0.2315935243,
0.2475191392,
0.357368123,
0.0951739556,
0.2239492207,
0.1609979725,
0.1964405335    
            ],
            'g':[
0.1424865544,
0.08642936792,
0.2208560994,
0.240512632,
0.09508285112,
0.1721748883,
0.2878452704,
0.1658111075,
0.21404219 
            ],             
            'r':[
0.1635831109,
0.2438391337,
0.1932553634,
0.149167438,
0.0937815623,
0.0964107049,
0.2035017705,
0.1064156087,
0.3311685509   
            ]
            }

from scipy import optimize, signal
import numpy as np
import time
import sympy as sy
import scipy.integrate as integrate
# from IPython.display import display, Math
import matplotlib.pyplot as plt
# from .convolv import g
# from scipy.signal import tria

# def test_func(x, dist, amp, omega, phi):
#     return dist + amp * np.cos(omega * x + phi)

# print('Original parameters:')
# display(Math('a_0={:.2f}, a_1={:.2f}, \\omega={:.2f}, \\phi={:.2f}'.format(*[10.0, 5.0, 3.0, 2.0])))


def sin_harm_2nd_with_w1(x, a0, a1, w1, phi1):
    # a1 = 0.8
    # a2 = 0.8
    # # phi2 = phi1
    # w1 = 2 * np.pi / 3600
    return a0 + a1 * np.sin(w1 * x + phi1)

def chi_square_error(y_true, y_pred):
    return sum(np.divide(np.square(y_true - y_pred), y_true))


if __name__ == "__main__":
    t = [0, 0, 0, 0]
    a_opt = [0, 0, 0, 0]
    for k, band in enumerate(['z', 'i', 'g', 'r']):
        def sawtooth(x, a1, phi1, q):
            w1 = 2 * np.pi / (3600*i)
            a0 = 14.3
            # q =0.5
            if k==0:
                a0 = 14.18
                # q = 0.5
            elif k==1:
                a0 = 14.2
                # q = 0.3
            elif k==2:
                a0 = 14.7030
                # q = 0.4
            elif k==3:
                a0 = 14.15
                # q = 0.5

            return signal.sawtooth(w1 * x + phi1, q) * a1 + a0
        
        def sin_harm_2nd(x, a1, phi1, a2, phi2):
            # a0 = 14.3
            w1 = 2 * np.pi / (3600*i)
            if k==0:
                a0 = 14.3070
                # w2 = 0.5
            elif k==1:
                a0 = 14.2903
                # w2 = 0.32
            elif k==2:
                a0 = 14.7030
                # w2 = 0.28
            elif k==3:
                a0 = 14.1269
                # w2 = 0.29
            # a0 = (max(y_data[band])+min(y_data[band]))/2
            # return signal.sawtooth(w1 * x + phi1, w2) * a1 + a0
            return a0 + a1 * np.sin(w1 * x + phi1) + a2 * np.sin( 2* w1 * x + phi2)

        def g(x, a1, phi, lambda_, sigma):
            a0 = 14.3
            # a0 = min(y_data[band])
            # w = 1
            # w1 = 2*np.pi/(3600*i)
            # t = sy.Symbol('t')
            # lambda_ = 1
            # sigma = 1
            # print("haha")
            return np.array(list(map(lambda x: a0 + a1*integrate.quad(lambda t: np.exp(-lambda_ * t) * np.exp(t-x%(3600*i) + phi)**2/(2*sigma*sigma), 0, 50), x)))
        
        # g = np.vectorize(g)

        def per_gaus(x, a1, phi, kappa, a2):
            w = 2*np.pi/(3600*i)
            a0 = min(y_data[band])
            # if k==0:
            #     a0 = 14.5
            #     # w2 = 0.5
            # elif k==1:
            #     a0 = 14.6
            #     # w2 = 0.32
            # elif k==2:
            #     a0 = 14.8
            #     # w2 = 0.28
            # elif k==3:
            #     a0 = 14.6
            #     # w2 = 0.29
            return a0 + a1*np.exp(kappa*np.cos(w*x + phi))/(1 + kappa**2/4 + kappa**4/64) + a2*np.exp(kappa*np.cos(w*x + phi - np.pi))/(1 + kappa**2/4 + kappa**4/64)

        error = np.inf
        # for a in np.arange(13.6, 14.9, 0.1):
        for i in np.arange(4, 14, 0.2):
            param_bounds=([-np.inf,-np.inf,0],[np.inf,np.inf,1])
            params, params_covariance = optimize.curve_fit(sawtooth, x_data[band], y_data[band],  maxfev=100000, sigma=y_error[band], bounds=param_bounds)
  
            # params, params_covariance = optimize.curve_fit(sin_harm_2nd, x_data[band], y_data[band],  maxfev=100000, sigma=y_error[band])

            x_data[band] = np.array(x_data[band])
            # y_fit1 = sin_harm_2nd(np.arange(min(x_data[band]), max(x_data[band]), 200), *params)
            # y_fit2 = sin_harm_2nd(x_data[band], *params)

            # y_fit1 = g(np.linspace(min(x_data[band]), max(x_data[band]), 30), *params)
            # y_fit2 = g(x_data[band], *params)

            # y_fit1 = per_gaus(np.linspace(min(x_data[band]), max(x_data[band]), 30), *params)
            # y_fit2 = per_gaus(x_data[band], *params)

            y_fit1 = sawtooth(np.linspace(min(x_data[band]), max(x_data[band]), 30), *params)
            y_fit2 = sawtooth(x_data[band], *params)

            # print('chi_square_error({}):'.format(band))

            if (error - chi_square_error(y_data[band], y_fit2) > 1e-6) :
                error = chi_square_error(y_data[band], y_fit2)
                t[k] = i
                # a_opt[k] = a

            # print('Fitted parameters({}):'.format(band))
            # print(params)

            import seaborn as sns
            sns.set_theme()
            plt.gca().invert_yaxis() 

            plt.errorbar(x_data[band], y_data[band], yerr=y_error[band], marker='s', label='data with error')
            # plt.plot(np.arange(min(x_data[band]), max(x_data[band]), 200), y_fit1, label='fit')
            plt.plot(np.linspace(min(x_data[band]), max(x_data[band]), 30), y_fit1, label='fit')
            plt.plot(x_data[band], y_fit2, label='fit (only at data points))')
            plt.legend(loc='best')

            plt.title('Band({})\ntime: {:.2f}; chi_square error: {:.5f}'.format(band, i, error))
            plt.savefig('sawtooth_'+band+'.png')
            plt.close()

            ### uncomment this after you have a good fit and fill it with the values you found
            if k==0 and abs(t[k]-7.8)<0.01:
                break
            if k==1 and abs(t[k]-12.4)<0.01:
                break
            if k==2 and abs(t[k]-11.4)<0.01:
                break
            if k==3 and abs(t[k]-8)<0.01:
                break



            # time.sleep(1)



    print(t, a_opt)
