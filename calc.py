import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
from sin import y_data, x_data

mass_sun = 1.989e30
radius_sun = 6.957e8
lum_sun = 3.828e26
temp_sun = 5778
mag_sun = 4.83


#period luminosity relation for RR Lyrae stars

## Cite "The RR Lyrae Instability Strip and the Distance Scale" by Marconi and Clementini (2005)
# a_V = 0.75 ± 0.03
# b_V = 0.23 ± 0.05
def period_lum(period):
    #absolute magnitude in V band
    # mag = -1.096 - 2.43*(math.log10(period/24) - 0.127)
    mag = -.961 - 2.73*(math.log10(period/24) - 0.127)

    z = 0.002
    mag =0.4711-1.1318*math.log10(period/24)+ 0.2053*math.log10(z)
    # mag = -0.23 + 0.75*(math.log10(period/24))
    return mag

def mag_lum(mag):
    lum = lum_sun*(10**((mag_sun-mag)/2.5))
    return lum

def radius(period):
    # radius = radius_sun*(10**(0.75*math.log10(period/24)-0.38))
    # radius = 2*radius_sun*math.sqrt(period/24)
    Z = 0.002
    radius = 10**(0.774 + 0.58*math.log10(period/24) - 0.035*math.log10(Z)) * radius_sun
    return radius

def mass(lum):
    # l/l. = 16.7 (m/m.)^0.93 
    # mass = mass_sun*(10**(0.61-1.25*math.log10(period/24)))
    mass = mass_sun*(lum/(16.7*lum_sun))**(1/.93)
    return mass

def temp(lum, radius):
    temp = (lum/(4*math.pi*radius**2*5.67e-8))**(1/4)
    return temp   

def distance(abs_mag, app_mag):
    dist = 10**((app_mag-abs_mag+5)/5)
    return dist

def spectral_type(temp):
    if temp >= 30000:
        return 'O'
    elif temp >= 10000:
        return 'B'
    elif temp >= 7500:
        return 'A'
    elif temp >= 6000:
        return 'F'
    elif temp >= 5200:
        return 'G'
    elif temp >= 3700:
        return 'K'
    elif temp >= 2400:
        return 'M'
    elif temp >= 1000:
        return 'L'
    elif temp >= 500:
        return 'T'
    else:
        return 'Y'
    


import csv

period_dict = {} 
with open('periods.csv', mode ='r')as file:
    csvFile = csv.reader(file)

    i= 0
    for lines in csvFile:
        if i==0:
            i+=1
            continue
        else:
            name = lines[0]
            period_z = float(lines[1].split('(')[0].split(' ')[0])
            period_i = float(lines[2].split('(')[0].split(' ')[0])
            period_g = float(lines[3].split('(')[0].split(' ')[0])
            period_r = float(lines[4].split('(')[0].split(' ')[0])
            i+=1
        
        period_dict[name] = [period_z, period_i, period_g, period_r]

# for key in period_dict:
#     print("Method: " + key)

#     print("Period: " + str([period_dict[key][i] for i in range(4)]))
    
#     abs_mag_z = [period_lum(period_dict[key][i]) for i in range(4)]
#     print("Apparent Magnitude: " + str([14.3 for i in range(4)]))
#     print("Abs Magnitude: " + str(abs_mag_z))

#     lum_z = [mag_lum(abs_mag_z[i]) for i in range(4)]
#     print("Luminosity: " + str(lum_z))

#     radius_z = [radius(period_dict[key][i]) for i in range(4)]
#     print("Radius: " + str(radius_z))

#     mass_z = [mass(lum_z[i]) for i in range(4)]
#     print("Mass: " + str(mass_z))

#     temp_z = [temp(lum_z[i], radius_z[i]) for i in range(4)]
#     print("Temperature: " + str(temp_z))

#     spectral_type_z = [spectral_type(temp_z[i]) for i in range(4)]
#     print("Spectral type: " + str(spectral_type_z))

#     # print(list(y_data.items())[i][1])
#     distance_z = [distance(abs_mag_z[i], 14.3) for i in range(4)]
#     print("Distance(pc): " + str(distance_z))
#     print("Parallax: " + str(1000*1/np.array(distance_z)) + " milli-arcsec")

#     print("---------------------------------")

period = (10.2+11+12.8)/3
abs_mag = period_lum(period)
lum = mag_lum(abs_mag)
radius = radius(period)
mass = mass(lum)
temp = temp(lum, radius)
spectral_type = spectral_type(temp)
distance = distance(abs_mag, 14.3)
print("Average Period: " + str(period))
print("Average Apparent Magnitude: " + str(14.3))
print("Average Abs Magnitude: " + str(abs_mag))
print("Average Luminosity: " + str(lum/lum_sun))
print("Average Radius: " + str(radius/radius_sun))
print("Average Mass: " + str(mass))
print("Average Temperature: " + str(temp))
print("Average Spectral type: " + str(spectral_type))
print("Average Distance(pc): " + str(distance))
print("Average Parallax: " + str(1000*1/distance) + " milli-arcsec")
