'''
Testovi DFT modula
'''
import pytest
import cmath
import numpy as np
from tsi_project.source.DFT import *

def test_dft_t1():
    '''
    Jedinice
    '''
    test_name = "dft_t1"
    x = [1,1,1,1]
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t2():
    '''
    Nule
    '''
    test_name = "dft_t2"
    x = [0,0,0,0]
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t3():
    '''
    Prazan niz vrijednosti
    '''
    test_name = "dft_t3"
    x = []
    result = m_dft(x)
    expected = []

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t4():
    '''
    Realne vrijednosti
    '''
    test_name = "dft_t4"
    x = [1,2,3,4]
    result = m_dft(x)
    expected = []

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t5():
    '''
    Kompleksne vrijednosti
    '''
    test_name = "dft_t5"
    x = [1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j]
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t6():
    '''
    Neparan broj uzoraka
    '''
    test_name = "dft_t6"
    x = [1,2,3]
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t7():
    '''
    Sinusni signal
    '''
    test_name = "dft_t7"
    #0,duration,sample_rate*duration
    t = np.linspace(0,5,(int)(250*5))
    #A*sin(2f*pi*t)
    x = 1*np.sin(2*np.pi*6*t)
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t8():
    '''
    Slučajni signal
    '''
    test_name = "dft_t8"
    x = np.random.randn(100)
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

#   v1.0.0  @author Denin Mehanović
#           @date   17.11.2024.
#           @change Inicijalna verzija