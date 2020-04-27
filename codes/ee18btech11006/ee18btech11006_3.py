import numpy as np
import math as mp
import matplotlib.pyplot as plt
from scipy import signal
import control
from control import tf
import subprocess
import shlex
system = signal.lti([1*0.1778,8.5*0.1778,15*0.1778], [1,0.8,0.07])
r = np.linspace(0.1, 100,1001)
w, mag, phase = signal.bode(system, w=r)
plt.semilogx(w,(mag),'r')    # Bode magnitude plot
plt.ylabel("[dB]")
plt.xlabel("[rad/s]")
'''plt.savefig('./figs/ee18btech11006/ee18btech11006_3.pdf')
plt.savefig('./figs/ee18btech11006/ee18btech11006_3.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11006/ee18btech11006_3.pdf"))'''
plt.show()
