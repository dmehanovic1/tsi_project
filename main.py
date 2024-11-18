'''
Scratch
'''
import numpy as np
from tsi_project.source.DFT import *
from tsi_project.source.plotter import *

t = np.linspace(0,1,(int)(20*1))
x = 1*np.sin(2*np.pi*1*t)
X = m_dft(x)

m_plot3(t, x, X)

t = np.linspace(0,1,(int)(20*1))
x = 1*np.cos(2*np.pi*1*t)
X = m_dft(x)

m_plot3(t, x, X)



