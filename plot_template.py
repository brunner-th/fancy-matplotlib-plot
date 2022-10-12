# -*- coding: utf-8 -*-

#-----------------------------------------------------------------
#
# name: thomas brunner
# email: brunner.th@hotmail.com
# nr: 12018550
#
#-----------------------------------------------------------------

from math import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# colors: k, firebrick, lightgrey, darkorange, seagreen, royalblue, rebeccapurple, orchid
# linestyle: "--"  "-." ":"
# marker: "o", "v", "^", "1", "2", "+", "x"

plt.rcParams['figure.figsize'] = [5.0, 5.0]
plt.rcParams['figure.dpi'] = 400

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

tick_spacing_major = 1
tick_spacing_minor = 0.25


x_vec = np.linspace(-3,3,30)
y1_vec = np.sin(x_vec)
y2_vec = np.cos(x_vec)
y3_vec = -np.cos(x_vec)

fig, ax = plt.subplots(1, figsize=(6, 4))
plt.title("Titel")

plt.plot(x_vec, y3_vec, color="k", label=r'$I_{C1}$', marker = "1", markersize = 5, linestyle = " ")
#plt.errorbar(x_vec, y1_vec, yerr = 0.2 , marker= ',', fmt='o', markersize=1, capsize=3, linewidth= 0.8, color="black")
plt.errorbar(x_vec, y1_vec, xerr = 0.05, yerr = 0.15 , label = r"$I_{L}$", fmt=',', markersize=1, capsize=2, linewidth= 0.8, color="black")


plt.plot(x_vec, y2_vec, color="k", label=r'$\delta_{C2}$',linewidth = 1, linestyle = "-.")
plt.fill_between(x_vec, np.add(y2_vec,np.linspace(0.05,0.4,len(x_vec))), np.add(y2_vec,np.linspace(-0.05,-0.4,len(x_vec))), color = "skyblue", edgecolor="k", linewidth=0.5)


plt.legend()
plt.xlabel('Zeit $t$ / s', size=10)
plt.ylabel('Strom $I_{x}$ / mA', size=10)
ax.set(xlim=(-3, 3))
ax.set(ylim=(-2, 2))

ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_major))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing_minor))
ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing_major))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing_minor))
ax.tick_params(axis='both', which='major', labelsize=10)
ax.tick_params(axis='both', which='minor', labelsize=8)

#ax.xaxis.set_tick_params(width=5)
#ax.yaxis.set_tick_params(width=5)

#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
#ax.spines['top'].set_color('none')

ax.legend(loc = 'upper left', frameon=False)

#ax.axhline(0, color='k', linewidth = 0.5)
#ax.axvline(0, color='k', linewidth = 0.5)

ax.grid(linestyle = ":", linewidth = 0.8)
#ax.grid(axis='x')
#ax.grid(axis='y')

plt.show()