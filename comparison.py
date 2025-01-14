import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from tsi_project.source.DFT import *
from tsi_project.source.FFT_rdx2 import *
from tsi_project.source.FFT_rdx4 import *
from tsi_project.source.plotter import *
from scipy.io import wavfile

import time

x = import_audio_n_samples(1,2**20, "C:/Workspace/TKM/TKM1/TSI/Projekt/venv/tsi_project/media/StarWars60.wav")
print(len(x))

t1 = time.time()
X = np.fft.fft(x)
t2 = time.time()
print("NP.FFT: " + (str)(t2-t1))

t1 = time.time()
try:
    X = m_fft_rdx2(x)
except:
    print("not applicable for rdx 2")
t2 = time.time()
print("FFT_rdx2: " + (str)(t2-t1))

t1 = time.time()
X = m_fft_rdx4(x)
t2 = time.time()
print("FFT_rdx4: " + (str)(t2-t1))
'''
t1 = time.time()
X = m_dft(x)
t2 = time.time()
print("DFT: " + (str)(t2-t1))
'''


#m_plot3(t, x, X)
#m_3dplot(X)
#m_env3dplot2(X)

