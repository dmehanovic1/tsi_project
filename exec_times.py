'''
Application for execution time comparison between different algorithms implemented. 500 iterations.
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from tsi_project.source.DFT import *
from tsi_project.source.FFT_rdx2 import *
from tsi_project.source.FFT_rdx4 import *
from tsi_project.source.plotter import *
from scipy.io import wavfile

import time

all = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
rdx4 = [2,4,6,8,10,12,14,16,18,20]
dft = [1,2,3,4,5,6,7,8,9,10,11]

cumul_time_internal = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cumul_time_fft2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cumul_time_fft4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cumul_time_dft = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

n = 500
it = n
while it > 0:
    it = it - 1;
    print('\n')
    print(it)
    for pwr in all:
        print(pwr)
        x = import_audio_n_samples(1, 2**pwr, "C:/Workspace/TKM/TKM1/TSI/Projekt/venv/tsi_project/media/StarWars60.wav")

        #internal
        t1 = time.time()
        X = np.fft.fft(x)
        t2 = time.time()
        diff1 = (t2 - t1)
        tmp = cumul_time_internal[pwr-1]
        tmp = tmp + diff1
        cumul_time_internal[pwr-1] = tmp
        #print(diff1)

        #fft2
        t1 = time.time()
        X = m_fft_rdx2(x)
        t2 = time.time()
        diff2 = (t2 - t1)
        tmp = cumul_time_fft2[pwr-1]
        tmp = tmp + diff2
        cumul_time_fft2[pwr-1] = tmp
        #print(diff2)

        diff3 = ""
        if pwr in rdx4:
            #fft4
            t1 = time.time()
            X = m_fft_rdx4(x)
            t2 = time.time()
            diff3 = (t2 - t1)
            tmp = cumul_time_fft4[pwr-1]
            tmp = tmp + diff3
            cumul_time_fft4[pwr-1] = tmp
        else:
            diff3 = "x"
        #print(diff3)

        diff4 = ""
        if pwr in dft:
            #dft
            t1 = time.time()
            X = m_dft(x)
            t2 = time.time()
            diff4 = (t2 - t1)
            tmp = cumul_time_dft[pwr-1]
            tmp = tmp + diff4
            cumul_time_dft[pwr-1] = tmp
        else:
            diff4 = "x"
        #print(diff4)

cumul_time_internal = [x/n for x in cumul_time_internal]
cumul_time_fft2 = [x/n for x in cumul_time_fft2]
cumul_time_fft4 = [x/n for x in cumul_time_fft4]
cumul_time_dft = [x/n for x in cumul_time_dft]

print(cumul_time_internal)
print(cumul_time_fft2)
print(cumul_time_fft4)
print(cumul_time_dft)