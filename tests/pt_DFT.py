import pytest
import cmath
import numpy as np
from tsi_project.source.DFT import *

def test_dft_t1():
    test_name = "dft_t1"
    x = [1,1,1,1]
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t2():
    test_name = "dft_t2"
    x = [0,0,0,0]
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t3():
    test_name = "dft_t3"
    x = []
    result = []
    expected = []
    error = "test"
    try:
        result = m_dft(x)
    except ValueError as e:
        error = e

    if error == ValueError("All elements of the list or np.ndarray must be numeric values (int or float or complex)."):
        expected = error

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t4():
    test_name = "dft_t4"
    x = [1,2,3,4]
    result = m_dft(x)
    expected = []

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t5():
    test_name = "dft_t5"
    x = [1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j]
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t6():
    test_name = "dft_t6"
    x = [1,2,3]
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t7():
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
    test_name = "dft_t8"
    x = np.random.randn(100)
    result = m_dft(x)
    expected = np.fft.fft(x)

    for r, e in zip(result, expected):
        assert abs(r-e) < 1e-6, f"{test_name}: Expected {e}, but got {r}"

def test_dft_t9():
    test_name = "dft_t9"
    x = ["1,1,1,1","b"]
    error = "ValueError"
    result = []
    try:
        result = m_dft(x)
    except ValueError as e:
        error = e
        if error == ValueError("Input must be a list or np.ndarray."):
            assert 1, f"{test_name}: {error}"

def test_dft_t10():
    test_name = "dft_10"
    x = 1
    result = []
    try:
        result = m_dft(x)
    except ValueError as e:
        assert 1,  f"{test_name}: {e}"


#   v1.0.0  @author Denin Mehanović
#           @date   17.11.2024.
#           @change Inicijalna verzija

#   v1.0.1  @author Amina Omerčević
#           @date   09.12.2024.
#           @change Uklonjen docstrings i dodani testovi za provjeru unosa
