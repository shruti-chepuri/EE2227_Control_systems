'''
Code by C Shruti
April 27,2020
Released under GNU GPL
'''
import numpy as np
import math as mp
import matplotlib.pyplot as plt
from scipy import signal
import control
from control import tf
#if using termux
import subprocess
import shlex
#end if
system = signal.lti([1,8.5,15], [1,0.8,0.07])
r = np.linspace(0.1, 100,1001)
w, mag, phase = signal.bode(system, w=r)
plt.semilogx(w,(mag))    # Bode magnitude plot
plt.title('Bode plot of Transfer Function')
plt.ylabel("[dB]")
plt.xlabel("[rad/s]")
#if using termux
plt.savefig('./figs/ee18btech11006/ee18btech11006_2.pdf')
plt.savefig('./figs/ee18btech11006/ee18btech11006_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11006/ee18btech11006_2.pdf"))
#end if
#plt.show()

