'''
Scratch
'''
import numpy as np
from tsi_project.source.DFT import *
from tsi_project.source.plotter import *
from scipy.io import wavfile

t = np.linspace(0,1,(int)(20*1))
x = 1*np.sin(2*np.pi*1*t)
X = m_dft(x)

m_plot3(t, x, X)

t = np.linspace(0,1,(int)(20*1))
x = 1*np.cos(2*np.pi*1*t)
X = m_dft(x)

m_plot3(t, x, X)

#from file
samp_rate, x = wavfile.read("C:/Workspace/TKM/TKM1/TSI/Projekt/venv/tsi_project/media/StarWars60.wav")
from_sec = 1
to_sec = 5 #seconds of the recording
x = x[from_sec*samp_rate:to_sec*samp_rate]
t = np.arange(len(x))/samp_rate
#X = m_dft(x)
X = np.fft.fft(x)

m_plot3(t, x, X)


