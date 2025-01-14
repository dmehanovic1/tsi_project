'''
Scratch
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from tsi_project.source.DFT import *
from tsi_project.source.FFT_rdx2 import *
from tsi_project.source.FFT_rdx4 import *
from tsi_project.source.plotter import *
from scipy.io import wavfile

x = [1+1j,1+1j,1+2j,1+1j]
#res1 = m_dft(x)
#res2 = m_fft_rdx2(x)
#res3 = m_fft_rdx4(x)
#print(x)
#print(res1)
#print(res2)
#print(res3)

#m_3dplot(res1)
#m_plot3([0,1,2,3], x, res1)
#m_env3dplot2(res1)


'''
t = np.linspace(0,1,(int)(20*1))
x = 1*np.sin(2*np.pi*1*t)
X = m_dft(x)

m_plot3(t, x, X)

t = np.linspace(0,1,(int)(20*1))
x = 1*np.cos(2*np.pi*1*t)
X = m_dft(x)

m_plot3(t, x, X)
'''
#from file
#samp_rate, x = wavfile.read("C:/Workspace/TKM/TKM1/TSI/Projekt/venv/tsi_project/media/StarWars60.wav")
#from_sec = 1
#to_sec = 5 #seconds of the recording
#x = x[from_sec*samp_rate:to_sec*samp_rate]
#t = np.arange(len(x))/samp_rate
#X = m_dft(x)
#X = np.fft.fft(x)

from_sec = 0
to_sec = 60
x = import_audio_n_samples(1,2**8, "C:/Workspace/TKM/TKM1/TSI/Projekt/venv/tsi_project/media/StarWars60.wav")
print(x)
print(len(x))
print(type(x[1]))
X = m_fft_rdx2(x)
#X = m_dft(x)


#m_plot3(t, x, X)
m_3dplot(X)
#m_env3dplot2(X)

